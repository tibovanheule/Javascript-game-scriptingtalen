#!/usr/bin/python

import cgi
import cgitb
import json
import random
import os

cgitb.enable()
print("Content-type: application/json\n\n")


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
        moves += i
    return list(set(moves))


def new_game(size=5):
    board = []
    moves = []
    colors = ["red", "green", "blue", "yellow", "purple"]
    for i in range(0, size):
        row = []
        for j in range(0, size):
            rand = random.randint(1, 100) % len(colors)
            row.append(colors[rand])
            if colors[rand] not in moves:
                moves.append(colors[rand])
        board.append(row)

    return json.dumps({"score": "0", "moves": [moves], "board": [board]}, indent=4)


def do_move(status, zet, plaats):
    board = status["board"][0]
    old = board[0][0]
    score = int(status["score"])
    if old != zet:
        if isover(board):
            return json.dumps(
                {"message": 'Spel is over, goed gespeeld! voltooid in ' + str(score) + ' stappen', "score": score,
                 "moves": [availablemove(board)],
                 "board": [board]}, indent=4)
        else:
            score = int(status["score"]) + 1
            new_board = check_move(board, zet, [0, 0], old)
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


if os.environ['REQUEST_METHOD'] == 'POST':
    parameters = cgi.FieldStorage()
    board1 = json.loads(parameters.getvalue("status"))
    zet1 = json.loads(parameters.getvalue("zet"))
    print(do_move(board1, zet1, [0, 0]))

if os.environ['REQUEST_METHOD'] == 'GET':
    print(new_game())
