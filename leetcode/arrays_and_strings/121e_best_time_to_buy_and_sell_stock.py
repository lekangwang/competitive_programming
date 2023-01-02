# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # only non-negative integers
        # array at least 1 in length
        curr_min, max_profit = prices[0], 0

        for p in prices:
            if p < curr_min:
                curr_min = p
            else:
                if p - curr_min > max_profit:
                    max_profit = p - curr_min
        
        return max_profit