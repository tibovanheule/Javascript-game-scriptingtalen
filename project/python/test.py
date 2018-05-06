import gekleurde_druppels


def is_over_test():
    assert isover([["red", "red", "red"], ["red", "red", "red"], ["red", "red", "red"]]) is True
    assert isover([["red", "red", "red"], ["red", "red", "red"], ["red", "blue", "red"]]) is False
