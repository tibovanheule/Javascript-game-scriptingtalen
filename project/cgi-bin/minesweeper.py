#!/usr/bin/python

import random
import json
import cgi
import os
import cgitb

cgitb.enable()
print("Content-type: application/json\n\n")


def new_game(size=10):
    board = []
    for j in range(size):
        row = ["uncovered"] * size
        for i in range(random.randint(size // 3, size // 2)):
            x = int(random.randint(0, 1000) % size) - 1
            row[x] = "mine-uncovered"
        board.append(row)
    for i in range(len(board)):
        for j in range(len(board[i])):
            aantal = 0
            x = i
            y = j
            if (y - int(1)) >= 0 and board[x][y - 1] == "mine-uncovered":
                aantal += 1
            if (x - int(1)) >= 0 and board[x - 1][y] == "mine-uncovered":
                aantal += 1
            if (y + int(1)) < len(board[0]) and board[x][y + 1] == "mine-uncovered":
                aantal += 1
            if (x + int(1)) < len(board) and board[x + 1][y] == "mine-uncovered":
                aantal += 1
            if aantal > 0 and not board[i][j] == "mine-uncovered":
                board[i][j] = "uncovered-" + str(aantal)
    return json.dumps({"board": [board], "score": "0", "moves": [["blank", "mijn"]]}, indent=4)


def isover(board):
    pos = ["mine-uncovered", "uncovered", "uncovered-1", "uncovered-2", "uncovered-3", "uncovered-4"]
    if not board:
        return True
    for i in board:
        for j in i:
            if j in pos:
                return False
    return True


def availablemove(board):
    moves = ["blank"]
    for i in board:
        for j in i:
            if j == 'mine-uncovered' and "mijn" not in moves:
                moves.append("mijn")
    return moves


def mijn(board, plaats):
    x = int(plaats[0])
    y = int(plaats[1])
    return board[x][y] == "mine-uncovered"


def do_move(status, zet, plaats):
    try:
        board = status["board"][0]
        x = int(plaats[0])
        y = int(plaats[1])
        score = int(status["score"])

        if mijn(board, plaats):
            if zet == "blank":
                return json.dumps(
                    {"message": 'verloren, u heeft op een mijn geklikt,' + str(score) + ' mijnen gevonden',
                     "score": score,
                     "moves": [availablemove(board)],
                     "board": [board]}, indent=4)
            else:
                score += 1
                board[x][y] = "mine-discovered"
                if isover(board):
                    return json.dumps(
                        {"message": 'Spel is over, goed gespeeld! alle ' + str(score) + ' mijnen gevonden!',
                         "score": score,
                         "moves": [availablemove(board)],
                         "board": [board]}, indent=4)
                else:
                    return json.dumps(
                        {"score": score, "moves": [availablemove(board)], "board": [board]},
                        indent=4)
        elif zet == "mijn":
            return json.dumps(
                {"message": 'verloren, was geen mijn,' + str(score) + ' mijnen gevonden',
                 "score": score,
                 "moves": [availablemove(board)],
                 "board": [board]}, indent=4)
        score = int(status["score"])
        new_board = check_move(board, zet, plaats, )
        if isover(new_board):
            return json.dumps(
                {"message": 'Spel is over, goed gespeeld! alle ' + str(score) + ' mijnen gevonden!',
                 "score": score, "moves": [availablemove(board)],
                 "board": [board]}, indent=4)
        else:
            return json.dumps(
                {"score": score, "moves": [availablemove(new_board)], "board": [new_board]},
                indent=4)

    except Exception as e:
        print(e)


def check_move(board, zet, plaats):
    x = int(plaats[0])
    y = int(plaats[1])
    if board[x][y] == "uncovered":
        board[x][y] = "discovered"
    for i in range(1, 5):
        if board[x][y] == "uncovered-" + str(i):
            board[x][y] = "discovered-" + str(i)
    old = ["uncovered", "uncovered-1", "uncovered-2", "uncovered-3", "uncovered-4"]
    checked = [[False] * len(board[0])] * len(board)
    if (y - int(1)) >= 0 and board[x][y - 1] in old and checked[x][y - int(1)] is False:
        checked[x][y - 1] = True
        board = check_move(board, zet, [x, y - 1])
    if (x - int(1)) >= 0 and board[x - 1][y] in old and checked[x - 1][y] is False:
        checked[x - 1][y] = True
        board = check_move(board, zet, [x - 1, y])
    if (y + int(1)) < len(board[0]) and board[x][y + int(1)] in old and checked[x][y + int(1)] is False:
        checked[x][y + int(1)] = True
        board = check_move(board, zet, [x, y + int(1)])
    if (x + int(1)) < len(board) and board[x + int(1)][y] in old and checked[x + 1][y] is False:
        checked[x + int(1)][y] = True
        board = check_move(board, zet, [x + int(1), y])
    return board


if os.environ['REQUEST_METHOD'] == 'POST':
    parameters = cgi.FieldStorage()
    board1 = json.loads(parameters.getvalue("status"))
    zet1 = json.loads(parameters.getvalue("zet"))
    plaats1 = json.loads(parameters.getvalue("plaats"))
    print(do_move(board1, zet1, plaats1))

if os.environ['REQUEST_METHOD'] == 'GET':
    print(new_game())
