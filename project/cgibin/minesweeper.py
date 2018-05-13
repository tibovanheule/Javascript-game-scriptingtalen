#!/usr/bin/python

import random
import json

print("Content-type: application/json\n\n")


def new_game(size=10):
    board = []
    for j in range(size):
        row = ["uncovered"] * size
        for i in range(random.randint(size // 3, size // 2) ):
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


try:
    print(new_game())
except Exception as e:
    print(e)
