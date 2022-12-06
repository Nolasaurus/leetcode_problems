class Solution:
    def maxProfit(self, prices: list[int]) -> int:

        max_p = 0
        min_value = 10**99

        for i, curr_price in enumerate(prices):
            
            if prices[i] < min_value:
                min_value = prices[i] ## list not empty
                
            elif prices[i]-min_value > max_p:
                max_p = prices[i] - min_value

        return max_p    