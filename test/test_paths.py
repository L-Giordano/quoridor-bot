import unittest
from src.player.player import Player
from src.player import paths


class Test_paths(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.path = [[(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 8), (7, 8), (8, 8)], [(2, 4), (2, 5), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6), (8, 6), (8, 7), (8, 8)], [(3, 3), (4, 3), (5, 3), (7, 3), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)], [(3, 5), (4, 5), (5, 5), (6, 5), (7, 5), (8, 5), (8, 6), (8, 7), (8, 8)], [(4, 4), (5, 4), (6, 4), (7, 4), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]]  # noqa: E501
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
                    "board": "                N                                    -               |S|    N          -                    N S N                               N                                                                 S                                                             S                ",  # noqa: E501
                    "turn_token": "087920d0-0e6b-4716-9e77-add550a006aa",
                    "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
                }
            }

        self.player = Player(self.request_data, "N")

    def test_calc_path(self):
        expected = self.path
        result = paths.calc_path(self.player)
        self.assertEqual(result, expected)

    # path_score func can't be tested because the key 'score'
    # contains a ramdomly float added

    # def test_path_score(self):
    #     expected = self.scored_paths
    #     result = paths.path_score(self.path, 'N')
    #     self.assertEqual(result, expected)
