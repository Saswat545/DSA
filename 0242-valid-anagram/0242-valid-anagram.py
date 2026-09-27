class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False 
        freq = dict()
        for i in s:
            freq[i] = freq.get(i,0)+1
        for i in t:
            if i not in freq:
                return False 
            else:
                if freq[i]==0: return False
                else:
                    freq[i] -= 1
        return True