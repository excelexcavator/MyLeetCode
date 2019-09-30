class Solution(object):
    def maxProfit(self, prices):
        """
            :type prices: List[int]
            :rtype: int
            """
        if len(prices) <= 1:
            return 0
        minprice = prices[0]
        maxprofit = 0
        totalprofit = 0
        for i in range(1,len(prices)):
            if prices[i] < prices[i-1]:
                totalprofit += maxprofit
                maxprofit = 0
                minprice = prices[i]
            else:
                maxprofit = prices[i]-minprice
        return totalprofit + maxprofit
