# https://leetcode.com/problems/first-missing-positive/solutions/?orderBy=most_votes

def firstMissingPositive(nums):
    nums.append(0) # append 0 for the case that length = 1 or answer = length + 1
    length = len(nums)
    for i in range(length): # filter to only positive numbers
        if nums[i] < 0 or nums[i] >= length:
            nums[i] = 0
    # record that a number (nums[i]) has occured by adding length to nums[i]%length
    # since our possible answer space is 1:n+1, an index where nums[i] / length < 1 then the index is our answer (because it hasn't had length added to it)
    # start iterating at 1 because 0 can't be our answer
    for i in range(length):
        nums[nums[i]%length] += length
    for i in range(1,length):
        if nums[i] / length < 1:
            return i
    # if all indices have had length added to it, length is our answer
    return length

assert firstMissingPositive(nums=[1,2,0]) == 3
assert firstMissingPositive(nums=[1,2,3]) == 4
