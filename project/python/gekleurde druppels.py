#!/usr/bin/python

import cgi
import cgitb
import random
import json

cgitb.enable()

print("Content-type: application/json\n\n")
parameters = cgi.FieldStorage()


def isover(board):
    for i in board:
        for j in i:
            if j != board[0][0]:
                return False
    return True


def availablemove(board):
    moves=[]
    for i in board:
        for j in i:
            if j not in moves:
                moves.append(j)


def new_game(size=5):
    board = []
    moves = []
    colors = ["red", "green", "blue", "yellow"]
    for i in range(0, size):
        row = []
        for j in range(0, size):
            rand = random.randint(1, 100) % len(colors)
            row.append(colors[rand])
            if colors[rand] not in moves:
                moves.append(colors[rand])
        board.append(row)

    return json.dumps({"message": '', "score": 0, "moves": [moves], "board": [board]}, indent=4)


def do_move(board, zet, plaats):
    moves = []
    score = parameters.getvalue("score")
    score += 1
    message = ""
    if isover(board):
        message = f"Congratulations, you completed te game in {score}!"

    return json.dumps({"message": message, "score": 0, "moves": [moves], "board": [board]}, indent=4)


print(new_game())
