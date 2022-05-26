import random
import networkx as nx


def calc_path(player):
    # print(33)
    player_pos = player.pawn_pos
    goal_pos = player.goal_pos
    q_graph = player.graph

    paths = []
    # print(44)
    # search all the best path between the pawns pos and the goal positions
    # nx.astar_path return a list with all the steps in the path
    # the first element of the list is the pawn pos
    for i in range(len(player_pos)):
        for j in range(len(goal_pos)):
            try:
                paths.append(
                        list(nx.astar_path(
                            q_graph, player_pos[i], goal_pos[j], weight=1)))  # noqa: E501
            except Exception:
                continue
        # print(55)
    # in case there are not possible paths
    # returns only one path with a lateral move and a high score
        random_move = 1 if random.randint(0, 2) > 1 else -1

        alt_paths = [(player_pos[i][0], player_pos[i][1]), (player_pos[i][0], (player_pos[i][1] + random_move))]  # noqa: E501
        # print(66)
        for i in range(18):
            alt_paths.append((0, 0))
        # print(77)
        paths = paths if len(paths) > 0 else alt_paths

    return paths


def path_score(paths, side):

    scored_paths = []
    # for each path returns the first two positions
    # the first pos contains the coor of the pawn(from_row, from_col)
    # the second pos contains the coor of the move(to_row, to_col)
    for i in range(len(paths)):
        score = {
            'player': side,
            'score': len(paths[i])+random.random(),
            'data': {
                'from_row': paths[i][0][0],
                'from_col': paths[i][0][1],
                'to_row': paths[i][1][0],
                'to_col': paths[i][1][1],
            },
        }
        scored_paths.append(score)
    return scored_paths
