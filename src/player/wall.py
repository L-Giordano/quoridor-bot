import logging
import networkx as nx
from networkx.exception import NetworkXError, NetworkXNoPath
import copy


def create_wall(path, own_player, opp_player):

    positions_data = {
            'own_pawns': own_player.pawn_pos,
            'own_goals': own_player.goal_pos,
            'oop_pawns': opp_player.pawn_pos,
            'oop_goals': opp_player.goal_pos
    }

    own_wall_graph = copy.deepcopy(own_player.graph)
    opp_wall_graph = copy.deepcopy(opp_player.graph)

    from_row = path['from_row']
    from_col = path['from_col']
    to_row = path['to_row']
    to_col = path['to_col']

    orientation = move_orientation(from_row, from_col, to_row, to_col)

    edges_to_rm = find_edges_to_remove(from_row, from_col, to_row, to_col, orientation)  # noqa: E501

    removed_edges = remove_egde(opp_wall_graph, own_wall_graph, positions_data, edges_to_rm)  # noqa: E501

    created_wall = wall_coor(removed_edges) if removed_edges is not None else None  # noqa: E501

    return created_wall


def move_orientation(from_row, from_col, to_row, to_col):

    if from_row > to_row:
        return 'n'

    if from_row < to_row:
        return 's'

    if from_col < to_col:
        return 'e'

    if from_col > to_col:
        return 'w'


# Selects the edge to remove from the graph to create the wall
# returns a list of tuples. The first position is the coor of the wall
# thats interrumps the opp pawn move.
# the second and the third pos of the list contains the coor of the wall
# on both sides of the first wall.
def find_edges_to_remove(from_row, from_col, to_row, to_col, orientation):

    response = []
    if orientation == 's':
        response.append(((from_row, from_col), (to_row, to_col)))  # wall to the south # noqa: E501
        response.append(((from_row, from_col - 1), (to_row, to_col - 1)))  # wall to the south-west # noqa: E501
        response.append(((from_row, from_col + 1), (to_row, to_col + 1)))  # wall to the south-east # noqa: E501

        return response

    if orientation == 'n':
        response.append(((to_row, to_col), (from_row, from_col)))  # wall to the north # noqa: E501
        response.append(((to_row, to_col - 1), (from_row, from_col - 1)))  # wall to the north-west # noqa: E501
        response.append(((to_row, to_col + 1), (from_row, from_col + 1)))  # wall to the north-east # noqa: E501

        return response

    if orientation == 'e':
        response.append(((from_row, from_col), (to_row, to_col)))  # wall to the east # noqa: E501
        response.append(((from_row - 1, from_col), (to_row - 1, to_col)))  # wall to the north-east # noqa: E501
        response.append(((from_row + 1, from_col), (to_row + 1, to_col)))  # wall to the south-east # noqa: E501

        return response

    if orientation == 'w':
        response.append(((to_row, to_col), (from_row, from_col)))  # wall to the west # noqa: E501
        response.append(((to_row - 1, to_col), (from_row - 1, from_col)))  # wall to the south-west # noqa: E501
        response.append(((to_row + 1, to_col), (from_row + 1, from_col)))  # wall to the north-west # noqa: E501

        return response


def remove_egde(opp_wall_graph, own_wall_graph, positions_data, edges_to_rm):

    if(opp_wall_graph.has_edge(edges_to_rm[1][0], edges_to_rm[1][1])):
        try:
            opp_wall_graph.remove_edge(edges_to_rm[0][0], edges_to_rm[0][1])
            opp_wall_graph.remove_edge(edges_to_rm[1][0], edges_to_rm[1][1])
            own_wall_graph.remove_edge(edges_to_rm[0][0], edges_to_rm[0][1])
            own_wall_graph.remove_edge(edges_to_rm[1][0], edges_to_rm[1][1])
        except NetworkXError as e:
            logging.exception(e)
            pass
        if verify_wall(opp_wall_graph, own_wall_graph, positions_data):
            return ((edges_to_rm[0], edges_to_rm[1]))

    if(opp_wall_graph.has_edge(edges_to_rm[2][0], edges_to_rm[2][1])):
        try:
            opp_wall_graph.add_edge(edges_to_rm[1][0], edges_to_rm[1][1])  # over roll # noqa: E501
            opp_wall_graph.remove_edge(edges_to_rm[2][0], edges_to_rm[2][1])
            own_wall_graph.add_edge(edges_to_rm[1][0], edges_to_rm[1][1])  # over roll # noqa: E501
            own_wall_graph.remove_edge(edges_to_rm[2][0], edges_to_rm[2][1])

        except NetworkXError as e:
            logging.exception(e)
            return None

        if verify_wall(opp_wall_graph, own_wall_graph, positions_data):
            return ((edges_to_rm[0], edges_to_rm[2]))
        else:
            return None


def verify_wall(opp_wall_graph, own_wall_graph, positions_data):

    opp_pawn_free = 0
    player_pawn_free = 0

    own_pawns = positions_data['own_pawns']
    own_goals = positions_data['own_goals']
    opp_pawns = positions_data['oop_pawns']
    opp_goals = positions_data['oop_goals']

    for i in range(len(opp_pawns)):
        for j in range(len(opp_goals)):
            try:
                nx.astar_path(opp_wall_graph, opp_pawns[i], opp_goals[j], weight=1)  # noqa: E501
                opp_pawn_free += 1
                break
            except NetworkXNoPath:
                continue

    for i in range(len(own_pawns)):
        for j in range(len(own_goals)):
            try:
                nx.astar_path(own_wall_graph, own_pawns[i], own_goals[j], weight=1)  # noqa: E501
                player_pawn_free += 1
                break
            except NetworkXNoPath:
                continue

    return opp_pawn_free > 2 and player_pawn_free > 2


def wall_coor(rm_edges):

    edge1, edge2 = rm_edges

    orientation = 'h' if edge1[0][0] == edge2[0][0] else 'v'
    if orientation == 'h':
        row = edge1[0][0]
        col = edge1[0][1] if edge1[0][1] < edge2[0][1] else edge2[0][1]

        return [orientation, row, col]

    if orientation == 'v':
        col = edge1[0][1]
        row = edge1[0][0] if edge1[0][0] < edge2[0][0] else edge2[0][0]

        return [orientation, row, col]
