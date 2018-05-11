import pytest


# functions used in other documents
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


def check_move(board, zet, plaats, old):
    x = int(plaats[0])
    y = int(plaats[1])
    board[x][y] = zet
    checked = [[False] * len(board[0])] * len(board)
    if (y + int(1)) < len(board[0]) and board[x][y + int(1)] == old and checked[x][y + int(1)] is False:
        checked[x][y + int(1)] = True
        board = check_move(board, zet, [x, y + int(1)], old)
    if (x + int(1)) < len(board) and board[x + int(1)][y] == old and checked[x + 1][y] is False:
        checked[x + int(1)][y] = True
        board = check_move(board, zet, [x + int(1), y], old)
    if (y - int(1)) >= 0 and board[x][y - 1] == old and checked[x][y - int(1)] is False:
        checked[x][y - 1] = True
        board = check_move(board, zet, [x, y - 1], old)
    if (x - int(1)) >= 0 and board[x - 1][y] == old and checked[x - 1][y] is False:
        checked[x - 1][y] = True
        board = check_move(board, zet, [x - int(1), y], old)
    return board


# The tests

# test methode is over
def test_is_over():
    assert isover([["red", "red", "red"], ["red", "red", "red"], ["red", "red", "red"]]) is True
    assert isover([["red", "red", "red"], ["red", "red", "red"], ["red", "blue", "red"]]) is False
    assert isover([]) is True


# test methode available moves
def test_available_moves():
    board1 = [["red", "blue", "green"], ["yellow", "red", "red"], ["red", "red", "red"]]
    assert availablemove(board1) == ["red", "blue", "green", "yellow"]
    board2 = [["red", "red", "red"], ["red", "red", "red"], ["red", "red", "red"]]
    assert availablemove(board2) == ["red"]
    board2[0][0] = "blue"
    assert availablemove(board2) == ["blue", "red"]
    board2[2][2] = "yellow"
    assert availablemove(board2) == ["blue", "red", "yellow"]


# test move
def test_check_move():
    board1 = [["blue", "red", "purple", "red", "yellow"], ["purple", "blue", "purple", "blue", "purple"],
              ["red", "purple", "blue", "purple", "blue"], ["purple", "yellow", "blue", "blue", "yellow"],
              ["purple", "green", "blue", "red", "green"]]
    answer1 = [["blue", "red", "purple", "red", "yellow"], ["purple", "blue", "purple", "blue", "purple"],
               ["red", "purple", "blue", "purple", "blue"], ["purple", "yellow", "blue", "blue", "yellow"],
               ["purple", "green", "blue", "red", "green"]]
    assert check_move(board1, "blue", [0, 0], "blue") == answer1
    answer1[0][0] = "purple"
    assert check_move(board1, "purple", [0, 0], "blue") == answer1
    board2 = [["red", "red", "red", "blue", "red"],
              ["red", "red", "red", "red", "red"],
              ["yellow", "green", "red", "green", "green"],
              ["red", "purple", "yellow", "red", "blue"],
              ["blue", "red", "green", "green", "green"]]
    answer2 = [["green", "green", "green", "blue", "green"],
               ["green", "green", "green", "green", "green"],
               ["yellow", "green", "green", "green", "green"],
               ["red", "purple", "yellow", "red", "blue"],
               ["blue", "red", "green", "green", "green"]]
    assert check_move(board2, "green", ["0", "0"], "red") == answer2
    board3 = [["purple", "purple", "blue", "purple", "purple"],
              ["purple", "purple", "purple", "purple", "purple"],
              ["purple", "purple", "purple", "purple", "purple"],
              ["purple", "yellow", "purple", "purple", "yellow"],
              ["blue", "green", "green", "purple", "purple"]]
    answer3 = [["blue", "blue", "blue", "blue", "blue"],
               ["blue", "blue", "blue", "blue", "blue"],
               ["blue", "blue", "blue", "blue", "blue"],
               ["blue", "yellow", "blue", "blue", "yellow"],
               ["blue", "green", "green", "blue", "blue"]]
    assert check_move(board3, "blue", ["0", "0"], "purple") == answer3
    answer4 = [["yellow", "yellow", "blue", "yellow", "yellow"],
              ["yellow", "yellow", "yellow", "yellow", "yellow"],
              ["yellow", "yellow", "yellow", "yellow", "yellow"],
              ["yellow", "yellow", "yellow", "yellow", "yellow"],
              ["blue", "green", "green", "yellow", "yellow"]]
    assert check_move(board3, "yellow", ["0", "0"], "purple") == answer4
