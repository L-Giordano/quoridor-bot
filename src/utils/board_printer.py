import logging


def board_printer(request_data):
    board = request_data['data']['board']
    newBoard = board.replace(" ", ".")

    logging.info('Player 1: %s', request_data['data']['player_1'])
    logging.info('Score player 1: %s', request_data['data']['score_1'])
    logging.info('Player 2: %s', request_data['data']['player_2'])
    logging.info('Score player 2: %s', request_data['data']['score_2'])
    logging.info('Your side: %s', request_data['data']['side'])
    logging.info('Remainig moves:%s', int(request_data['data']['remaining_moves']/2))  # noqa: E501

    print('  0a1b2c3d4e5f6g7h8')
    for i in range(17):
        if i % 2 == 0:
            print(int(i / 2), end="|")
        else:
            print(chr(97 + int(i / 2)), end="|")
        for j in range(17):
            if j == 16:
                print(newBoard[j + (i * 17)], "|")
            else:
                print(newBoard[j + (i * 17)], end="")
