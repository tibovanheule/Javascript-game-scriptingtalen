#!/usr/bin/python

import cgi
import json

print("Content-type: application/json\n\n")
parameters = cgi.FieldStorage()
board1 = json.loads(parameters.getvalue("board"))
zet1 = json.loads(parameters.getvalue("zet"))
plaats1 = json.loads(parameters.getvalue("plaats"))


def isover(board):
    if not board:
        return True
    for i in board:
        for j in i:
            if j != board[0][0]:
                return False
    return True


def availablemove(board):
    moves = []
    for i in board:
        for j in i:
            if j not in moves:
                moves.append(j)
    return moves


def do_move(board, zet, plaats):
    try:
        if isover(board):
            return json.dumps({"message": 'The game is over well played!', "score": 0, "moves": [availablemove(board)],
                               "board": [board]}, indent=4)
        else:
            x = int(plaats[0])
            y = int(plaats[1])
            old = board[x][y]
            if x == 0 and y == 0:

                new_board = check_move(board, zet, plaats, old)
                if isover(new_board):
                    return json.dumps(
                        {"message": 'The game is over well played!', "score": 0, "moves": [availablemove(board)],
                         "board": [board]}, indent=4)
                else:
                    return json.dumps(
                        {"message": '', "score": '1', "moves": [availablemove(new_board)], "board": [new_board]},
                        indent=4)
            return json.dumps({"message": '', "score": 0, "moves": [availablemove(board)], "board": [board]}, indent=4)

    except Exception as e:
        print(e)


def check_move(board, zet, plaats, old):
    x = int(plaats[0])
    y = int(plaats[1])
    board[x][y] = zet
    if (y + int(1)) < len(board[0]) and board[x][y + int(1)] == old:
        board[x][y + int(1)] = zet
        board = check_move(board, zet, [x, y + int(1)], old)
    if (x + int(1)) < len(board) and board[x + int(1)][y] == old:
        board[x + int(1)][y] = zet
        board = check_move(board, zet, [x + int(1), y], old)
    if (y - int(1)) >= 0 and board[x][y - 1] == old:
        board[x][y - 1] = zet
    if (x - int(1)) >= 0 and board[x - 1][y] == old:
        board[x - 1][y] = zet
    return board


print(do_move(board1[0], zet1, plaats1))
