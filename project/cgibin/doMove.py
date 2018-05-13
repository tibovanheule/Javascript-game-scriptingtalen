#!/usr/bin/python

import cgi
import json

print("Content-type: application/json\n\n")
parameters = cgi.FieldStorage()
board1 = json.loads(parameters.getvalue("status"))
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


def do_move(status, zet, plaats):
    try:
        board = status["board"][0]
        x = int(plaats[0])
        y = int(plaats[1])
        old = board[x][y]
        score = int(status["score"])
        if x == 0 and y == 0 and old != zet:
            if isover(board):
                return json.dumps(
                    {"message": 'Spel is over, goed gespeeld! voltooid in ' + str(score) + ' stappen', "score": score,
                     "moves": [availablemove(board)],
                     "board": [board]}, indent=4)
            else:
                score = int(status["score"]) + 1
                new_board = check_move(board, zet, plaats, old)
                if isover(new_board):
                    return json.dumps(
                        {"message": 'Spel is over, goed gespeeld! voltooid in ' + str(score) + ' stappen',
                         "score": score, "moves": [availablemove(board)],
                         "board": [board]}, indent=4)
                else:
                    return json.dumps(
                        {"score": score, "moves": [availablemove(new_board)], "board": [new_board]},
                        indent=4)

        else:
            return json.dumps(
                {"score": score, "moves": [availablemove(board)], "board": [board]},
                indent=4)
    except Exception as e:
        print(e)


def check_move(board, zet, plaats, old):
    x = int(plaats[0])
    y = int(plaats[1])
    board[x][y] = zet
    checked = [[False] * len(board[0])] * len(board)
    if (y - int(1)) >= 0 and board[x][y - 1] == old and checked[x][y - int(1)] is False:
        checked[x][y - 1] = True
        board = check_move(board, zet, [x, y - 1], old)
    if (x - int(1)) >= 0 and board[x - 1][y] == old and checked[x - 1][y] is False:
        checked[x - 1][y] = True
        board = check_move(board, zet, [x - 1, y], old)
    if (y + int(1)) < len(board[0]) and board[x][y + int(1)] == old and checked[x][y + int(1)] is False:
        checked[x][y + int(1)] = True
        board = check_move(board, zet, [x, y + int(1)], old)
    if (x + int(1)) < len(board) and board[x + int(1)][y] == old and checked[x + 1][y] is False:
        checked[x + int(1)][y] = True
        board = check_move(board, zet, [x + int(1), y], old)
    return board


print(do_move(board1, zet1, plaats1))
