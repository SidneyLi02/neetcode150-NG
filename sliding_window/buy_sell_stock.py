class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0

        buy, sell = 0, 1
        max_profit = 0
        while sell < len(prices):
            curr_profit = prices[sell] - prices[buy]
            if curr_profit < 0:
                buy = sell
            else:
                max_profit = max(max_profit, curr_profit)
            sell += 1
        return max_profit
    
        """
        NOTE: 
        solution:                     O(n) time, O(1) space
        It can be shown this problem reduces to solving maximum cont.
        subarray sum, with the once-differenced array and Kadane's algorithm.
        """