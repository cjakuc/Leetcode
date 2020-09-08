class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i, v in enumerate(nums):
            if v in my_dict:
                my_dict[v] = [my_dict[v],i]
            else:
                my_dict[v] = i
        lst = []
        for num in nums:
            complement = target - num
            if complement == num and type(my_dict[num])!=list:
                continue
            elif complement == num and type(my_dict[num])==list:
                return my_dict[num]
            elif complement in my_dict:
                lst.append(my_dict[num])
                lst.append(my_dict[complement])
                return lst
