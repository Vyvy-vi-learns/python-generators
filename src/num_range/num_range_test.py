import pytest
from num_range.num_range import NumRange


def check_func(x: int) -> int:
    return (x + 1) * 2


def test_num_range_default():
    assert list(NumRange(10)) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_num_range_with_lambda_func():
    check_list = [0, 20, 40, 60, 80]
    assert list(NumRange(100, lambda x: x + 20)) == check_list


def test_num_range_with_custom_func():
    check_list = [0, 2, 6, 14, 30, 62]
    assert list(NumRange(100, check_func)) == check_list


def test_num_range_with_large_stop_arg():
    vals = []
    for i in range(100000000000000000000):
        vals.append(i)
        if i == 4:
            break
    assert vals == [0, 1, 2, 3, 4]
