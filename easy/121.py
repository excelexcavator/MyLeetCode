class Solution(object):
    def maxProfit(self, prices):
        """
            :type prices: List[int]
            :rtype: int
            """
        minprice = float('inf')
        maxprofit = 0
        for i in prices:
            if i < minprice:
                minprice = i
            else:
                maxprofit = max(maxprofit, i-minprice)
        return maxprofit
