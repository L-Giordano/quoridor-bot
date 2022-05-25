import networkx as nx
from networkx.exception import NetworkXError, NetworkXNoPath


def create_wall(path, o_wall_graph, p_wall_graph, o_data, p_data):

    from_row = path['from_row']
    from_col = path['from_col']
    to_row = path['to_row']
    to_col = path['to_col']

    orientation = move_orientation(from_row, from_col, to_row, to_col)

    edges_to_rm = edges_to_remove(from_row, from_col, to_row, to_col, orientation)  # noqa: E501

    response = remove_egde(o_wall_graph, p_wall_graph, o_data, p_data, edges_to_rm)  # noqa: E501

    return None if response is None else response


def remove_egde(o_wall_graph, p_wall_graph, o_data, p_data, edges_to_rm):

    if(o_wall_graph.has_edge(edges_to_rm[1][0], edges_to_rm[1][1])):
        try:
            o_wall_graph.remove_edge(edges_to_rm[0][0], edges_to_rm[0][1])
            o_wall_graph.remove_edge(edges_to_rm[1][0], edges_to_rm[1][1])
        except NetworkXError:
            pass
        if verify_wall(o_wall_graph, p_wall_graph, o_data, p_data):
            return wall_coor(edges_to_rm[0], edges_to_rm[1])

    if(o_wall_graph.has_edge(edges_to_rm[2][0], edges_to_rm[2][1])):
        try:
            o_wall_graph.add_edge(edges_to_rm[1][0], edges_to_rm[1][1])
            o_wall_graph.remove_edge(edges_to_rm[2][0], edges_to_rm[2][1])
        except NetworkXError:
            return None

        if verify_wall(o_wall_graph, p_wall_graph, o_data, p_data):
            return wall_coor(edges_to_rm[0], edges_to_rm[2])
        else:
            return None


def wall_coor(edge1, edge2):

    orientation = 'h' if edge1[0][0] == edge2[0][0] else 'v'
    if orientation == 'h':
        row = edge1[0][0]
        col = edge1[0][1] if edge1[0][1] < edge2[0][1] else edge2[0][1]

        return [orientation, row, col]

    if orientation == 'v':
        col = edge1[0][1]
        row = edge1[0][0] if edge1[0][0] < edge2[0][0] else edge2[0][0]

        return [orientation, row, col]


def verify_wall(o_wall_graph, p_wall_graph, o_data, p_data):

    opp_pawn_free = 0
    player_pawn_free = 0

    o_pawns = o_data['player_pos']
    o_goals = o_data['player_goal_pos']
    p_pawns = p_data['player_pos']
    p_goals = p_data['player_goal_pos']

    for i in range(len(o_pawns)):
        for j in range(len(o_goals)):
            try:
                nx.astar_path(o_wall_graph, o_pawns[i], o_goals[j], weight=1)
                opp_pawn_free += 1
                break
            except NetworkXNoPath:
                continue

    for i in range(len(p_pawns)):
        for j in range(len(p_goals)):
            try:
                nx.astar_path(p_wall_graph, p_pawns[i], p_goals[j], weight=1)
                player_pawn_free += 1
                break
            except NetworkXNoPath:
                continue

    return opp_pawn_free > 2 and player_pawn_free > 2


def move_orientation(from_row, from_col, to_row, to_col):

    if from_row > to_row:
        return 'n'

    if from_row < to_row:
        return 's'

    if from_col < to_col:
        return 'e'

    if from_col > to_col:
        return 'w'


def edges_to_remove(from_row, from_col, to_row, to_col, orientation):

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
