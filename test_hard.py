# import pytest

# from easy.romanToInt import romanToInt
from levels.hard import maximumSum

def test_maximumSum():
    assert maximumSum([3,3,9,9,5], 7) == 6
    assert maximumSum([1,2,3], 2) == 1
    assert maximumSum([1,5,9], 5) == 4
    assert maximumSum([3,2,7,4], 7) == 6