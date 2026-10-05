class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        l=0
        r=0
        maxp=0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r]-prices[l]
                maxp=max(maxp,profit)
            else:
                l=r
            r+=1
        return maxp