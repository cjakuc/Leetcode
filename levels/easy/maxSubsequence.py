# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/


def maxSubsequence(nums, k):
    # Create a 2D array of number and index and sort it reversed based on number
    val_and_index = sorted([(num, i) for i, num in enumerate(nums)])
    # Make a list of the K highest values
    return [num for num, i in sorted(val_and_index[-k:], key=lambda x: x[1])]


def testMaxSubsequence():
    assert maxSubsequence(nums = [2,1,3,3], k = 2) == [3, 3]
    assert maxSubsequence(nums = [-1,-2,3,4], k = 3) == [-1, 3, 4]
    assert maxSubsequence(nums = [3,4,3,3], k = 2) == [4, 3]

print(testMaxSubsequence())