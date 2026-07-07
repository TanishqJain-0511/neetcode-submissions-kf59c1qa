class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0

        for i in range(0, len(prices)):

            left = i
            right = i+1
            while right < len(prices):
                if prices[left] < prices[right]:
                    profit = max(profit, prices[right]-prices[left])
                right += 1
        return profit
