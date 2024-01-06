from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], -1, "default") == 3
    assert arrs.get([1, 2, 3], 10, "default") == "default"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3, 4], end=3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4, 5], start=-3, end=-1) == [3, 4]
    assert arrs.my_slice([], 0, 2) == []

