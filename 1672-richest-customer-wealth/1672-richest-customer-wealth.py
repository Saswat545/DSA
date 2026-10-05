class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_welth = 0
        for customers in accounts:
            customer_welth = sum (customers)
            max_welth = max(max_welth , customer_welth)
        return max_welth