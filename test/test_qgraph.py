import unittest
from src.graph.graphs import Q_graph
from src.player.player import Player


class Test_qgraph(unittest.TestCase):

    orth_graph = None
    diag_graph = None

    def setUp(self):
        self.orth_Req_data = {
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

        self.diag_Req_data = {
                "event": "your_turn",
                "data": {
                    "player_2": "uno",
                    "player_1": "dos",
                    "score_2": 0.0,
                    "walls": 10.0,
                    "score_1": 0.0,
                    "side": "N",
                    "remaining_moves": 50.0,
                    "board": "  N     S N|           -          N S  |N|                     -      S   S   S N|           -   -     |N|    N          -             -     |N S N|    N                         N       S        -   -    S          |N S              -    N             S N-                     |N S     N  ",  # noqa: E501
                    "game_id": "ab16e71c-caeb-11eb-975e-0242c0a80004"
                }
            }

        self.orth_graph = Q_graph()
        self.orth_board = Player.str_board_to_matrix(self.orth_Req_data['data']['board'])  # noqa: E501
        self.diag_graph = Q_graph()
        self.diag_board = Player.str_board_to_matrix(self.diag_Req_data['data']['board'])  # noqa: E501

    # valid othogonal moves
    def test_f_south_orth_vt(self):
        result = self.orth_graph.f_south_orth_vt(12, 6, self.orth_board, 'N')
        self.assertEqual(result, [((6, 3), (7, 3))])

    def test_f_north_orth_vt(self):
        result = self.orth_graph.f_north_orth_vt(12, 6, self.orth_board, 'N')
        self.assertEqual(result, [((6, 3), (5, 3))])

    def test_f_east_orth_vt(self):
        result = self.orth_graph.f_east_orth_vt(12, 6, self.orth_board, 'N')
        self.assertEqual(result, [((6, 3), (6, 4))])

    def test_f_west_orth_vt(self):
        result = self.orth_graph.f_west_orth_vt(12, 6, self.orth_board, 'N')
        self.assertEqual(result, [((6, 3), (6, 2))])

    # out of bounds moves
    def test_south_out_of_bounds(self):
        result = self.orth_graph.f_south_orth_vt(16, 0, self.orth_board, 'N')
        self.assertEqual(result, [])

    def test_west_out_of_bounds(self):
        result = self.orth_graph.f_west_orth_vt(16, 0, self.orth_board, 'N')
        self.assertEqual(result, [])

    def test_north_out_of_bounds(self):
        result = self.orth_graph.f_north_orth_vt(0, 16, self.orth_board, 'N')
        self.assertEqual(result, [])

    def test_east_out_of_bounds(self):
        result = self.orth_graph.f_east_orth_vt(0, 16, self.orth_board, 'N')
        self.assertEqual(result, [])

    # orthogonal blocked cell
    def test_south_blocked(self):
        result = self.orth_graph.f_south_orth_vt(4, 2, self.orth_board, 'N')
        self.assertEqual(result, [])

    def test_north_blocked(self):
        result = self.orth_graph.f_north_orth_vt(4, 2, self.orth_board, 'N')
        self.assertEqual(result, [])

    def test_east_blocked(self):
        result = self.orth_graph.f_east_orth_vt(4, 2, self.orth_board, 'N')
        self.assertEqual(result, [])

    def test_west_blocked(self):
        result = self.orth_graph.f_west_orth_vt(4, 2, self.orth_board, 'N')
        self.assertEqual(result, [])

    # orthogonal jump
    def test_south_jump(self):
        result = self.orth_graph.f_south_orth_vt(6, 8, self.orth_board, 'N')
        self.assertEqual(result, [((3, 4), (5, 4))])

    def test_north_jump(self):
        result = self.orth_graph.f_north_orth_vt(6, 8, self.orth_board, 'N')
        self.assertEqual(result, [((3, 4), (1, 4))])

    def test_east_jump(self):
        result = self.orth_graph.f_east_orth_vt(6, 8, self.orth_board, 'N')
        self.assertEqual(result, [((3, 4), (3, 6))])

    def test_west_jump(self):
        result = self.orth_graph.f_west_orth_vt(6, 8, self.orth_board, 'N')
        self.assertEqual(result, [((3, 4), (3, 2))])

    # diagonal moves
    def test_south_diag_vt(self):
        result = self.diag_graph.f_south_diag_vt(8, 8, self.diag_board, 'N')
        self.assertEqual(result, [((4, 4), (5, 5)), ((4, 4), (5, 3))])

    def test_north_diag_vt(self):
        result = self.diag_graph.f_north_diag_vt(8, 8, self.diag_board, 'N')
        self.assertEqual(result, [((4, 4), (3, 5)), ((4, 4), (3, 3))])

    def test_east_diag_vt(self):
        result = self.diag_graph.f_east_diag_vt(8, 8, self.diag_board, 'N')
        self.assertEqual(result, [((4, 4), (5, 5)), ((4, 4), (3, 5))])

    def test_west_diag_vt(self):
        result = self.diag_graph.f_west_diag_vt(8, 8, self.diag_board, 'N')
        self.assertEqual(result, [((4, 4), (5, 3)), ((4, 4), (3, 3))])

    # forbidden diagonal moves
    def test_forb_south_diag(self):
        result = self.diag_graph.f_south_diag_vt(14, 14, self.diag_board, 'N')
        self.assertEqual(result, [])

    def test_forb_north_diag(self):
        result = self.diag_graph.f_north_diag_vt(2, 2, self.diag_board, 'N')
        self.assertEqual(result, [])

    def test_forb_east_diag(self):
        result = self.diag_graph.f_east_diag_vt(14, 14, self.diag_board, 'N')
        self.assertEqual(result, [])

    def test_forb_west_diag(self):
        result = self.diag_graph.f_west_diag_vt(2, 2, self.diag_board, 'N')
        self.assertEqual(result, [])

    # out of bounds diagonal moves
    def test_oob_south_diag(self):
        result = self.diag_graph.f_south_diag_vt(12, 0, self.diag_board, 'N')
        self.assertEqual(result, [((6, 0), (7, 1))])

    def test_oob_north_diag(self):
        result = self.diag_graph.f_north_diag_vt(10, 16, self.diag_board, 'N')
        self.assertEqual(result, [((5, 8), (4, 7))])

    def test_oob_east_diag(self):
        result = self.diag_graph.f_east_diag_vt(0, 8, self.diag_board, 'N')
        self.assertEqual(result, [((0, 4), (1, 5))])

    def test_oob_west_diag(self):
        result = self.diag_graph.f_west_diag_vt(16, 8, self.diag_board, 'N')
        self.assertEqual(result, [((8, 4), (7, 3))])

    # blocked diagonal moves
    def test_blk_south_diag(self):
        result = self.diag_graph.f_south_diag_vt(4, 2, self.diag_board, 'N')
        self.assertEqual(result, [])

    def test_blk_north_diag(self):
        result = self.diag_graph.f_north_diag_vt(4, 6, self.diag_board, 'N')
        self.assertEqual(result, [])

    def test_blk_east_diag(self):
        result = self.diag_graph.f_east_diag_vt(4, 10, self.diag_board, 'N')
        self.assertEqual(result, [])

    def test_blk_west_diag(self):
        result = self.diag_graph.f_west_diag_vt(12, 14, self.diag_board, 'N')
        self.assertEqual(result, [])
