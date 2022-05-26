from networkx.classes import Graph


class Q_graph(Graph):
    def __init__(self, data=None, val=None, **attr):
        super(Q_graph, self).__init__()
        self.val = val
        self.is_built = True

    def set_opp(self, opp):
        self.opp = opp

    def set_board(self, board):
        self.board = board

    def create_graph(self):
        self.add_edges_from(self.add_edges())

    def add_edges(self):

        vertex = []
        for i in range(9):
            for j in range(9):
                row = i*2
                col = j*2

                vertex += self.f_south_orth_vt(row, col, self.board, self.opp)
                vertex += self.f_north_orth_vt(row, col, self.board, self.opp)
                vertex += self.f_east_orth_vt(row, col, self.board, self.opp)
                vertex += self.f_west_orth_vt(row, col, self.board, self.opp)
                vertex += self.f_south_diag_vt(row, col, self.board, self.opp)
                vertex += self.f_north_diag_vt(row, col, self.board, self.opp)
                vertex += self.f_east_diag_vt(row, col, self.board, self.opp)
                vertex += self.f_west_diag_vt(row, col, self.board, self.opp)

        return vertex

    def f_south_orth_vt(self, row, col, board, opp):
        vertex = []
        wr = row + 1  # wall row
        wc = col  # wall col
        lr = row + 2  # pawn row
        lc = col  # pawn col
        nwr = row + 3  # next wall row
        nwc = col  # next wall col
        nlr = row + 4  # next pawn row
        nlc = col  # next pawn col

        if ((row > len(board) - 3) or  # prevents out of bounds to the south # noqa: E501
            (board[row][col] == opp) or
                (board[wr][wc] == '-')):  # prevents blocked cell

            return vertex

        if (board[lr][lc] == ' '):  # landing cell is empty

            vertex.append(((row // 2, col // 2), (lr // 2, lc // 2)))
            return vertex

        # jumpping opp pawn
        if ((board[lr][lc] == opp) and  # landding cell occupied
            (nlr <= len(board) - 1) and  # prevents jump landing out of bounds # noqa: E501
            (board[nwr][nwc] == ' ') and  # no blocked new landing cell
                (board[nlr][nlc] == ' ')):  # empty landing cell

            vertex.append(((row // 2, col // 2), (nlr // 2, nlc // 2)))
            return vertex

        return vertex

    def f_north_orth_vt(self, row, col, board, opp):

        vertex = []

        wr = row - 1  # wall row
        wc = col  # wall col
        lr = row - 2  # pawn row
        lc = col  # pawn col
        nwr = row - 3  # next wall row
        nwc = col  # next wall col
        nlr = row - 4  # next pawn row
        nlc = col  # next pawn col

        if ((row < 2) or  # prevents out of bounds to the north
            (board[row][col] == opp) or
                (board[wr][wc] == '-')):  # prevents blocked cell

            return vertex

        if (board[lr][lc] == ' '):  # landing cell is empty

            vertex.append(((row // 2, col // 2), (lr // 2, lc // 2)))
            return vertex

        # jumpping opp pawn
        if ((board[lr][lc] == opp) and  # landding cell occupied
            (nlr >= 0) and  # prevents jump landing out of bounds
            (board[nwr][nwc] == ' ') and  # no blocked new landing cell
                (board[nlr][nlc] == ' ')):  # empty landing cell

            vertex.append(((row // 2, col // 2), (nlr // 2, nlc // 2)))
            return vertex

        return vertex

    def f_east_orth_vt(self, row, col, board, opp):

        vertex = []

        wr = row  # wall row
        wc = col + 1  # wall col
        lr = row  # pawn row
        lc = col + 2  # pawn col
        nwr = row  # next wall row
        nwc = col + 3  # next wall col
        nlr = row  # next pawn row
        nlc = col + 4  # next pawn col

        if ((col > len(board) - 3)  # prevents out of bounds to the east
            or (board[row][col] == opp)
                or (board[wr][wc] == '|')):  # prevents blocked cell

            return vertex

        if (board[lr][lc] == ' '):  # landing cell is empty

            vertex.append(((row // 2, col // 2), (lr // 2, lc // 2)))
            return vertex

        # jumpping opp pawn
        if ((board[lr][lc] == opp)  # landding cell occupied
            and (nlc <= len(board) - 1)  # prevents jump landing out of bounds # noqa: E501
            and (board[nwr][nwc] == ' ')  # no blocked new landing cell
                and (board[nlr][nlc] == ' ')):  # empty landing cell

            vertex.append(((row // 2, col // 2), (nlr // 2, nlc // 2)))
            return vertex

        return vertex

    def f_west_orth_vt(self, row, col, board, opp):

        vertex = []

        wr = row  # wall row
        wc = col - 1  # wall col
        lr = row  # pawn row
        lc = col - 2  # pawn col
        nwr = row  # next wall row
        nwc = col - 3  # next wall col
        nlr = row  # next pawn row
        nlc = col - 4  # next pawn col

        if ((col < 2)  # prevents out of bounds to the west
            or (board[row][col] == opp)
                or (board[wr][wc] == '|')):  # prevents blocked cell

            return vertex

        if (board[lr][lc] == ' '):  # landing cell is empty

            vertex.append(((row // 2, col // 2), (lr // 2, lc // 2)))
            return vertex

        # jumpping opp pawn
        if ((board[lr][lc] == opp)  # landding cell occupied
            and (nlc >= 0)  # prevents jump landing out of bounds
            and (board[nwr][nwc] == ' ')  # no blocked new landing cell
                and (board[nlr][nlc] == ' ')):  # empty landing cell

            vertex.append(((row // 2, col // 2), (nlr // 2, nlc // 2)))
            return vertex

        return vertex

    def f_south_diag_vt(self, row, col, board, opp):

        vertex = []

        wr = row + 1  # wall row
        wc = col  # wall col
        os_row = row + 2  # opp square row
        os_col = col  # opp square row
        bow_row = row + 3  # behind opp wal row
        bow_col = col  # behind opp wal col

        lper = row + 2  # diagonal landing pawn row to the east
        lpec = col + 2  # diagonal landing pawn row to the east
        dwer = row + 2  # diagonal wall row to the east
        dwec = col + 1  # diagonal wall col to the east

        lpwr = row + 2  # diagonal landing pawn row to the west
        lpwc = col - 2  # diagonal landing pawn row to the west
        dwwr = row + 2  # diagonal wall row to the west
        dwwc = col - 1  # diagonal wall col to the west

        if((row < len(board) - 3)  # prevents opp in the last row
            and (lpec <= len(board) - 1)  # prevents out of bounds to the east # noqa: E501
            and (board[wr][wc] == ' ')  # no blocked cell
            and (board[os_row][os_col] == opp)  # cel occupied by a opp pawn # noqa: E501
            and (board[bow_row][bow_col] == '-')  # wall behind opp pawn
            and (board[dwer][dwec] == ' ')  # no blocked diagonal
                and (board[lper][lpec] == ' ')):  # free landing cell

            vertex.append(((row // 2, col // 2), (lper // 2, lpec // 2)))

        if((row < len(board) - 3)  # prevents opp in the last row
            and (lpwc >= 0)  # prevents out of bounds to the west
            and (board[wr][wc] == ' ')  # no blocked cell
            and (board[os_row][os_col] == opp)  # cel occupied by a opp pawn # noqa: E501
            and (board[bow_row][bow_col] == '-')  # wall behind opp pawn
            and (board[dwwr][dwwc] == ' ')  # no blocked diagonal
                and (board[lpwr][lpwc] == ' ')):  # free landing cell

            vertex.append(((row // 2, col // 2), (lpwr // 2, lpwc // 2)))

        return vertex

    def f_north_diag_vt(self, row, col, board, opp):

        vertex = []

        wr = row - 1  # wall row
        wc = col  # wall col
        os_row = row - 2  # opp square row
        os_col = col  # opp square row
        bow_row = row - 3  # behind opp wal row
        bow_col = col  # behind opp wal col

        lper = row - 2  # diagonal landing pawn row to the east
        lpec = col + 2  # diagonal landing pawn row to the east
        dwer = row - 2  # diagonal wall row to the east
        dwec = col + 1  # diagonal wall col to the east

        lpwr = row - 2  # diagonal landing pawn row to the west
        lpwc = col - 2  # diagonal landing pawn row to the west
        dwwr = row - 2  # diagonal wall row to the west
        dwwc = col - 1  # diagonal wall col to the west

        if((row > 2)  # prevents opp in the last row
            and (lpec <= len(board) - 1)  # prevents out of bounds to the east # noqa: E501
            and (board[wr][wc] == ' ')  # no blocked cell
            and (board[os_row][os_col] == opp)  # cel occupied by a opp pawn # noqa: E501
            and (board[bow_row][bow_col] == '-')  # wall behind opp pawn
            and (board[dwer][dwec] == ' ')  # no blocked diagonal
                and (board[lper][lpec] == ' ')):  # free landing cell

            vertex.append(((row // 2, col // 2), (lper // 2, lpec // 2)))

        if((row > 2)  # prevents opp in the last row
            and (lpwc >= 0)  # prevents out of bounds to the west
            and (board[wr][wc] == ' ')  # no blocked cell
            and (board[os_row][os_col] == opp)  # cel occupied by a opp pawn # noqa: E501
            and (board[bow_row][bow_col] == '-')  # wall behind opp pawn
            and (board[dwwr][dwwc] == ' ')  # no blocked diagonal
                and (board[lpwr][lpwc] == ' ')):  # free landing cell

            vertex.append(((row // 2, col // 2), (lpwr // 2, lpwc // 2)))

        return vertex

    def f_east_diag_vt(self, row, col, board, opp):

        vertex = []

        wr = row  # wall row
        wc = col + 1  # wall col
        os_row = row  # opp square row
        os_col = col + 2  # opp square row
        bow_row = row  # behind opp wal row
        bow_col = col + 3  # behind opp wal col

        lpsr = row + 2  # diagonal landing pawn row to the south
        lpsc = col + 2  # diagonal landing pawn row to the south
        dwsr = row + 1  # diagonal wall row to the south
        dwsc = col + 2  # diagonal wall col to the south

        lpnr = row - 2  # diagonal landing pawn row to the north
        lpnc = col + 2  # diagonal landing pawn row to the north
        dwnr = row - 1  # diagonal wall row to the north
        dwnc = col + 2  # diagonal wall col to the north

        if((col < len(board) - 3)  # prevents opp in the last row
            and (lpsr <= len(board) - 1)  # prevents out of bounds to the south # noqa: E501
            and (board[wr][wc] == ' ')  # no blocked cell
            and (board[os_row][os_col] == opp)  # cel occupied by a opp pawn # noqa: E501
            and (board[bow_row][bow_col] == '|')  # wall behind opp pawn
            and (board[dwsr][dwsc] == ' ')  # no blocked diagonal
                and (board[lpsr][lpsc] == ' ')):  # free landing cell

            vertex.append(((row // 2, col // 2), (lpsr // 2, lpsc // 2)))

        if((col < len(board) - 3)  # prevents opp in the last row
            and (lpnr >= 0)  # prevents out of bounds to the north
            and (board[wr][wc] == ' ')  # no blocked cell
            and (board[os_row][os_col] == opp)  # cel occupied by a opp pawn # noqa: E501
            and (board[bow_row][bow_col] == '|')  # wall behind opp pawn
            and (board[dwnr][dwnc] == ' ')  # no blocked diagonal
                and (board[lpnr][lpnc] == ' ')):  # free landing cell

            vertex.append(((row // 2, col // 2), (lpnr // 2, lpnc // 2)))

        return vertex

    def f_west_diag_vt(self, row, col, board, opp):

        vertex = []

        wr = row  # wall row
        wc = col - 1  # wall col
        os_row = row  # opp square row
        os_col = col - 2  # opp square row
        bow_row = row  # behind opp wal row
        bow_col = col - 3  # behind opp wal col

        lpsr = row + 2  # diagonal landing pawn row to the south
        lpsc = col - 2  # diagonal landing pawn row to the south
        dwsr = row + 1  # diagonal wall row to the south
        dwsc = col - 2  # diagonal wall col to the south

        lpnr = row - 2  # diagonal landing pawn row to the north
        lpnc = col - 2  # diagonal landing pawn row to the north
        dwnr = row - 1  # diagonal wall row to the north
        dwnc = col - 2  # diagonal wall col to the north

        if((col > 2)  # prevents opp in the last row
            and (lpsr <= len(board) - 1)  # prevents out of bounds to the south # noqa: E501
            and (board[wr][wc] == ' ')  # no blocked cell
            and (board[os_row][os_col] == opp)  # cel occupied by a opp pawn # noqa: E501
            and (board[bow_row][bow_col] == '|')  # wall behind opp pawn
            and (board[dwsr][dwsc] == ' ')  # no blocked diagonal
                and (board[lpsr][lpsc] == ' ')):  # free landing cell

            vertex.append(((row // 2, col // 2), (lpsr // 2, lpsc // 2)))

        if((col > 2)  # prevents opp in the last row
            and (lpnr >= 0)  # prevents out of bounds to the north
            and (board[wr][wc] == ' ')  # no blocked cell
            and (board[os_row][os_col] == opp)  # cel occupied by a opp pawn # noqa: E501
            and (board[bow_row][bow_col] == '|')  # wall behind opp pawn
            and (board[dwnr][dwnc] == ' ')  # no blocked diagonal
                and (board[lpnr][lpnc] == ' ')):  # free landing cell

            vertex.append(((row // 2, col // 2), (lpnr // 2, lpnc // 2)))

        return vertex
