import math
import os
import random
import re
import sys
from bisect import bisect,insort

def maximumSum(arr):
    max_subsequence = arr[0]
    current_sub = arr[0]
    max_subarray = arr[0]
    for idx, x in enumerate(arr):
        if idx == 0:
            continue
        current_sub = max(x, current_sub + x)
        max_subarray = max(max_subarray, current_sub)
        max_subsequence = max(max_subsequence, x, max_subsequence + x)
    
    return [max_subarray, max_subsequence]


def test_maximumSum():
    assert maximumSum([1, 2, 3, 4]) == [10, 10]
    assert maximumSum([2, -1, 2, 3, 4, -5]) == [10, 11]
    assert maximumSum([-2, -3, -1, -4, -6]) == [-1, -1]
    assert maximumSum([-2, 2, -1, 3, -6]) == [4, 5]

print(test_maximumSum())