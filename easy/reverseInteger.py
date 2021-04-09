class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) >= 2**31-1:
            return 0
        temp = str(abs(x))
        temp = int(temp[::-1])
        if temp >= 2**31:
            return 0
        if x < 0:
            return -temp
        return temp
