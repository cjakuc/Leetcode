# https://leetcode.com/problems/maximum-subarray/

def maxSubArray(nums):
    current_sub = nums[0]
    max_subarray = nums[0]
    for idx, x in enumerate(nums):
        if idx == 0:
            continue
        current_sub = max(x, current_sub + x)
        max_subarray = max(max_subarray, current_sub)

    return max_subarray


def test_maxSubArray():
    assert maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert maxSubArray([1]) == 1
    assert maxSubArray([5,4,-1,7,8]) == 23

print(test_maxSubArray())