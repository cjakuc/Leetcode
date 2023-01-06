class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        letters = len(s)
        cycle = 2*numRows - 2
        strlst = []
        for i in range(numRows):
            # range(start=0, stop, step=1)
            for j in range(i, letters, cycle):
                strlst.append(s[j])
                if i != numRows-1 and i != 0 and j+cycle-2*i < letters:
                    strlst.append(s[j+cycle-2*i])
        newstr = ''.join(strlst)
        return newstr
