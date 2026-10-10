class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}
        for i in s:
            count[i] = count.get(i, 0) + 1
        for p,q in enumerate (s):
            if count[q]== 1:
                return p
        return -1