import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        full_list = nums1 + nums2
        full_list.sort()
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        length = nums1_length + nums2_length
        mid = math.floor(length/2)
        if length == 1:
            if nums1_length == 1:
                return nums1[0]
            else:
                return nums2[0]
        if length == 2:
            if nums1_length == 1:
                return (nums1[0] + nums2[0]) / 2
            elif nums1_length == 2:
                return (nums1[0] + nums1[1]) / 2
            else:
                return (nums2[0] + nums2[1]) / 2
        if length % 2 == 0:
            return (full_list[mid] + full_list[mid-1]) / 2
        else:
            return full_list[mid]
