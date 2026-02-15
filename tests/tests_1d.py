"""
tests_1d.py

Unit tests for two_sum in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum


def test_basic_case():
    nums = [2, 7, 11, 15]
    assert two_sum(nums, 26) == [2, 3]


def test_duplicates():
    nums = [3, 5, 3]
    assert two_sum(nums, 6) == [0, 2]


def test_negative_numbers():
    nums = [-3, -4, 3, 90]
    assert two_sum(nums, -1) == [1, 2]


def test_out_of_order():
    nums = [1, 5, 2, 4]
    assert two_sum(nums, 9) == [1, 3]


if __name__ == "__main__":
    pytest.main()
