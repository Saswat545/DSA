class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        i= nums[0]
        ans = -1
        for j in range (1,len(nums)):
            if nums[j] > i:
                ans = max(ans,nums[j]-i)
            else:
                i = nums[j]
        return ans