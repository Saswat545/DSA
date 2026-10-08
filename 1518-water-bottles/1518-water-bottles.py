class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ttl_drank = numBottles
        empty = numBottles
        while empty >= numExchange:
            exchange = empty // numExchange
            # exchange but got remainder 
            remain_ex = empty % numExchange
            ttl_drank = exchange + ttl_drank 
            empty = exchange + remain_ex
        return ttl_drank
