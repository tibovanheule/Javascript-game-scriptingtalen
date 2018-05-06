import pytest


def isover(board):
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


def test_isover():
    assert isover([["red", "red", "red"], ["red", "red", "red"], ["red", "red", "red"]]) is True
    assert isover([["red", "red", "red"], ["red", "red", "red"], ["red", "blue", "red"]]) is False


def test_availablemoves():
    assert availablemove([["red", "blue", "green"], ["yellow", "red", "red"], ["red", "red", "red"]]) == ["red", "blue",
                                                                                                          "green",
                                                                                                          "yellow"]
