class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left, right = 0, 1
        while left < len(prices) and right < len(prices):
            if prices[left] > prices[right]:
                left = right
                right = right + 1
            else:
                profit = max(profit, (prices[right] - prices[left]))
                right += 1
        return profit