from src.types_and_stuff import powerset, is_atonal

def test_powerset():
    assert powerset([1, 2, 3]) == [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert powerset([1, 2, 3, 4]) == [[1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]


def test_is_atonal():
    assert is_atonal([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]) == True
    assert is_atonal([0, 1, 2]) == True
    assert is_atonal([0, 2, 4]) == False
    assert is_atonal([0]) == False