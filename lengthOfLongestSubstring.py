class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        i = 0
        longest = s[0]
        while i < len(s):
            my_dict = {}
            temp = s[i]
            my_dict[s[i]] = ""
            for c in s[i+1:]:
                if c not in my_dict:
                    temp += c
                    my_dict[c] = ""
                    if len(temp) > len(longest):
                        longest = temp
                else:
                    break
            i += 1
        
        
        
        return len(longest)
