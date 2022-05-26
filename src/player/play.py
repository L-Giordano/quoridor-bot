
from src.player import player
from src.player import paths
from src.player import wall
from src.utils.response_formatter import format_action_your_turn
from src.utils.board_printer import board_printer


async def play(request_data):

    board_printer(request_data)
    # print(1)
    own_player = player.Player(request_data, request_data['data']['side'])
    opp_player = player.Player(request_data, 'S' if request_data['data']['side'] == 'N' else 'N')  # noqa: E501
    # print(2)

    own_paths = paths.calc_path(own_player)
    opp_paths = paths.calc_path(opp_player)

    scored_own_paths = paths.path_score(own_paths, own_player.side)
    scored_opp_paths = paths.path_score(opp_paths, opp_player.side)

    # own_paths = paths.Paths(own_player)
    # opp_paths = paths.Paths(opp_player)
    # print(3)
    # player and opp best paths sorted by lower score
    # add and sort the player and the opp scores
    all_scores = scored_own_paths + scored_opp_paths
    all_scores.sort(key=lambda path: path['score'])
    # print(4)
    selected_play = select_play(all_scores, request_data, own_player, opp_player)  # noqa: E501
    # print(5)
    # format the response before send it
    response = format_action_your_turn(request_data, selected_play)

    return response


def select_play(all_scores, request_data, own_player, opp_player):

    side = request_data['data']['side']
    remaining_walls = request_data['data']['walls']

    for i in range(len(all_scores)):

        if ((all_scores[i]['player'] != side)
                and (remaining_walls > 0)):

            wall_to_play = wall.create_wall(all_scores[i]['data'], own_player, opp_player)  # noqa: E501

            if (wall_to_play is None):
                continue

            else:
                return {
                    'action': 'wall',
                    'data': {
                        'row': wall_to_play[1],
                        'col': wall_to_play[2],
                        'orientation': wall_to_play[0]
                    }
                }
        else:
            return {
                'action': 'move',
                'data': {
                    'from_row': all_scores[i]['data']['from_row'],
                    'from_col': all_scores[i]['data']['from_col'],
                    'to_row': all_scores[i]['data']['to_row'],
                    'to_col': all_scores[i]['data']['to_col']
                }
            }
