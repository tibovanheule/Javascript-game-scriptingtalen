def isover(board):
    for i in board:
        for j in i:
            if j != board[0][0]:
                return False
    return True


def is_over_test():
    assert isover([["red", "red", "red"], ["red", "red", "red"], ["red", "red", "red"]]) is True
    assert isover([["red", "red", "red"], ["red", "red", "red"], ["red", "blue", "red"]]) is False
