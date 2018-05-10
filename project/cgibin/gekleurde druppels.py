#!/usr/bin/python

import cgi
import cgitb
import json
import random

cgitb.enable()

print("Content-type: application/json\n\n")
parameters = cgi.FieldStorage()


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


def new_game(size=5):
    board = []
    moves = []
    colors = ["red", "green", "blue", "yellow","purple"]
    for i in range(0, size):
        row = []
        for j in range(0, size):
            rand = random.randint(1, 100) % len(colors)
            row.append(colors[rand])
            if colors[rand] not in moves:
                moves.append(colors[rand])
        board.append(row)

    return json.dumps({"score": "0", "moves": [moves], "board": [board]}, indent=4)


print(new_game())
