class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = prices[0]
        profit = 0 

        for num in prices:
            min_price = min(min_price, num)
            profit = max(profit, num-min_price)

        return profit
