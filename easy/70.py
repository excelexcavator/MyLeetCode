class Solution(object):
    def climbStairs(self, n):
        """
            :type n: int
            :rtype: int
            """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        way = [1]*n
        way[1] = 2
        for i in range(2,n):
            way[i] = way[i-1]+way[i-2]
        return way[n-1]
