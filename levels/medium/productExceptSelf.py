# https://leetcode.com/problems/product-of-array-except-self/description/
from functools import reduce
from itertools import accumulate
from operator import mul

def productExceptSelf(nums):
    # Time Complexity : O(N)
    # Space Complexity : O(1)

    # prod excluding 0s
    # reduce applies the lambda to first two elements, then result w/ next element, etc.
    prod = reduce(lambda a, b: a*(b if b else 1), nums, 1)
    zero_cnt = nums.count(0)
    # If multiple 0s, prod except self is always 0
    if zero_cnt > 1:
        return [0]*len(nums)
    for i, c in enumerate(nums):
        if zero_cnt:
            if c != 0:
                nums[i] = 0
            else:
                nums[i] = prod
        else:
            # Have to use floor division aka integer division
            nums[i] = prod // c

    return nums


assert productExceptSelf(nums=[1,2,3,4]) == [24,12,8,6]
assert productExceptSelf(nums=[-1,1,0,-3,3]) == [0,0,9,0,0]

def productExceptSelfNoDivision(nums):
    # Time Complexity : O(N), calculating pre and suf arrays takes O(N) time and then another O(N) to compute ans. Total complexity comes out to be O(3*N) = O(N).
    # Space Complexity : O(N), required to store pre and suf arrays

    # Products moving forward
    prefix_array = list(accumulate(nums, mul))
    # Products moving backwards
    suffix_array = list(accumulate(nums[::-1], mul))[::-1]
    len_nums = len(nums)

    # W/ prefix and suffix arrays, loop through indices and save prod(prefix[:i-1]) * prod(suffix[i+1:]) (unless at beginning or end of array)
    # This works because constraint is len_nums >= 2
    # If it could be 1 or 0 then we would need if blocks to catch above
    final_array = []
    for i in range(len_nums):
        if i != 0:
            left = prefix_array[i-1]
        else:
            left = 1
        if i + 1 < len_nums:
            right = suffix_array[i+1]
        else:
            right = 1
        final_array.append(left * right)
    return final_array

    # Same as above in a list comprehension
    # return [(prefix_array[i-1] if i else 1) * (suffix_array[i+1] if i+1 < len_nums else 1) for i in range(len_nums)]

assert productExceptSelfNoDivision(nums=[1,2,3,4]) == [24,12,8,6]
assert productExceptSelfNoDivision(nums=[-1,1,0,-3,3]) == [0,0,9,0,0]
