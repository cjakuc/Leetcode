class Solution:
    def isPalindrome(self, x: int) -> bool:
        forward = str(x)
        backward = forward[::-1]
        return forward == backward
