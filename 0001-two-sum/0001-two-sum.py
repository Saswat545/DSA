class Solution(object):
    def twoSum(self, nums, target):
        prevmap=dict()
        for i , j in enumerate (nums):
            prevmap[j] = i
        for i,j in enumerate(nums):
            diff = target-j
            if diff in prevmap and prevmap[diff] != i:
                return [prevmap[diff],i] 