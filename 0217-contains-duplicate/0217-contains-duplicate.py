class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        harset=set()
        for i in nums:
            if i in harset:
                return True
            harset.add(i)
        return False