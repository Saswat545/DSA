class Solution(object):
    def isPalindrome(self, x):
        num = x
        result = 0
        while num>0:
            last_no= num%10
            result=(result*10)+last_no
            num = num//10
        return x==result