import math
import os
import random
import re
import sys
from bisect import bisect,insort

def maximumSum(a, m):
    # Overall time complexity is O(n log(n))
    # O(n) from the for loop
    # O(log n) from the bisect
    # O(n) from the insort insertion
    # O(n) * O(log n) * O(n) = O(n log n)

    len_a = len(a)
    prefix_array = []
    sum_so_far = 0
    max_sum = 0
    for idx in range(len_a):
        # Ex: a = [3,3,9,9,5] m = 7
        # sum_so_far = ((sum_so_far + a[idx]) % m) % m

        # iter 0 -> sum_so_far = (0 + 3) % 7 = 3 -> idx_to_subtract = 0 -> prefix_array = [3]
        # iter 1 -> sum_so_far = (3 + 3) % 7 = 6 -> idx_to_subtract = 1 -> prefix_array = [3, 6]
        # iter 2 -> sum_so_far = (6 + 9) % 7 = 1 -> idx_to_subtract = 0 -> prefix_array = [1, 3, 6]
        # iter 3 -> sum_so_far = (1 + 9) % 7 = 3 -> idx_to_subtract = 2 -> prefix_array = [1, 3, 3, 6]
        # iter 4 -> sum_so_far = (3 + 5) % 7 = 1 -> idx_to_subtract = 1 -> prefix_array = [1, 1, 3, 3, 6]

        sum_so_far = (sum_so_far + a[idx]) % m
        # bisect(bisect_right) locates the insertion point in a for x that would maintain sort order (lest to greatest)
        # bisect runs in 0(log n) time
        idx_to_subtract = bisect(a=prefix_array, x=sum_so_far)
        if idx_to_subtract == idx:
            d = 0
        else:
            d = prefix_array[idx_to_subtract]
        max_sum = max(max_sum, (sum_so_far - d + m) % m)
        insort(a=prefix_array, x=sum_so_far) # insort does bisect and inserts x into a -> the insertion is O(n) time

    return max_sum

def test_maximumSum():
    assert maximumSum([3,2], 7) == 5
    assert maximumSum([3,3,9,9,5], 7) == 6
    assert maximumSum([1,2,3], 2) == 1
    assert maximumSum([1,5,9], 5) == 4
    assert maximumSum([3,2,7,4], 7) == 6
    assert maximumSum([7,7,1,3], 9) == 8

print(test_maximumSum())