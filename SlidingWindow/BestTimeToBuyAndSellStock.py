class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                this_profit = prices[r] - prices[l]
                profit = max(profit, this_profit)
            else:
                l = r
            r += 1

        return profit