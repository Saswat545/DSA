class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        ht = {}
        ans = []

        for num in nums:
            ht[num] = ht.get(num, 0) + 1

        while k > 0:
            maxi = -1
            max_num = None

            for num in ht:
                if ht[num] > maxi:
                    maxi = ht[num]
                    max_num = num

            ans.append(max_num)
            del ht[max_num]
            k -= 1
        return ans