from src.types_and_stuff import powerset

def test_powerset():
    assert powerset([1, 2, 3]) == [[1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert powerset([1, 2, 3, 4]) == [[1], [2], [3], [4], [1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4], [1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]