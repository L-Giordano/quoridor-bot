import unittest
from src.player import player


class Test_player(unittest.TestCase):

    player = None
    matrix_board = None
    side = None

    def setUp(self):
        self.request_data = {
                "event": "your_turn",
                "data": {
                    "player_2": "uno",
                    "player_1": "dos",
                    "score_2": 0.0,
                    "walls": 10.0,
                    "score_1": 0.0,
                    "side": "N",
                    "remaining_moves": 50.0,
                    "board": "                N                             N                           N                                |   |   |         - -     - -     |   |   |                         |   |   |S                        |   |   |       - -                  S                                         S",  # noqa: E501
                    "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
                    "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
                }
            }
        self.player = player.Player(self.request_data, self.request_data['data']['side'])  # noqa: E501
        self.matrix_board = self.player.matrix_board
        self.side = self.player.side

    def test_find_paws_pos(self):
        expected = [(0, 8), (1, 6), (2, 3)]
        result = self.player.find_pawns_pos(self.matrix_board, self.side)
        self.assertEqual(result, expected)

    def test_find_goal_pos(self):
        expected = [(8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)]  # noqa: E501

        result = self.player.find_goal_pos(self.matrix_board, self.side)
        self.assertEqual(result, expected)
