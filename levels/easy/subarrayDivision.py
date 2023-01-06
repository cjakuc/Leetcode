import math
import os
import random
import re
import sys
from bisect import bisect,insort

def birthday(s, d, m):
    solution_count = 0
    for i in range(len(s)+m-1):
        if sum(s[i:i+m]) == d:
            solution_count += 1
    
    return solution_count


def test_birthday():
    assert birthday([1, 2, 1, 3, 2], 3, 2) == 2
    assert birthday([1, 1, 1, 1, 1, 1], 3, 2) == 0
    assert birthday([4], 4, 1) == 1
    # assert birthday()

print(test_birthday())