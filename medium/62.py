class Solution(object):
    def uniquePaths(self, m, n):
        """
            :type m: int
            :type n: int
            :rtype: int
            """
        grid = [[1 for x in range(m)] for y in range(n)]
        for i in range(1,m):
            for j in range(1,n):
                grid[j][i] = grid[j][i-1]+grid[j-1][i]
        return grid[-1][-1]
