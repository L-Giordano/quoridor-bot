import numpy as np
from src.graph import graphs


class Player():
    def __init__(self, request_data, player):
        self.request_data = request_data
        self.player = player
        self.side = 'S' if self.player == 'S' else 'N'
        self.opp_side = 'S' if self.side == 'N' else 'N'
        self.matrix_board = self.str_board_to_matrix(request_data['data']['board'])  # noqa: E501
        self.pawn_pos = self.find_pawns_pos(self.matrix_board, self.side)
        self.goal_pos = self.find_goal_pos(self.matrix_board, self.side)
        self.graph = self.create_q_graph(self.opp_side, self.matrix_board)

    @staticmethod
    def str_board_to_matrix(str_board):
        matrix_board = np.array(list(str_board), dtype=str)
        matrix_board = matrix_board.reshape(17, 17)
        return matrix_board

    def find_pawns_pos(self, matrix_board, side):
        pawn_positions = []
        for i in range(9):
            for j in range(9):
                if matrix_board[i * 2][j * 2] == side:
                    pawn_positions.append((i, j))

        return pawn_positions

    def find_goal_pos(self, matrix_board, side):
        goal_row = 16 if side == 'N' else 0
        goal_positions = []
        for i in range(9):
            if matrix_board[goal_row][i*2] == " ":
                goal_positions.append((goal_row//2, i))
        return goal_positions

    def create_q_graph(self, o_side, matrix_board):

        q_graph = graphs.Q_graph()
        q_graph.set_board(matrix_board)
        q_graph.set_opp(o_side)
        q_graph.create_graph()

        return q_graph
