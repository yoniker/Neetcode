class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #The only thing that "interests" any price at any time is what's the maximumu price to its right. Therefore, i'll keep a pointer to current max value toe the right, and then traverse the array from right to left. If I'll encounter a bigger price while traversing left, save it since this is the only thing interesting to all nodes to its left, not the previous maximum.

        current_max_price=prices[-1]
        current_max_profit = 0 
        for i in range(len(prices)-1,-1,-1):
            if current_max_profit<current_max_price-prices[i]:
                current_max_profit = current_max_price-prices[i]
            if current_max_price < prices[i]:
                current_max_price = prices[i]
        return current_max_profit
