class Solution(object):
    def minPathSum(self, grid):
        """
            :type grid: List[List[int]]
            :rtype: int
            """
        if not grid:
            return 0
        for i in range(len(grid)):
            if i > 0:
                grid[i][0] += grid[i-1][0]
            for j in range(1, len(grid[0])):
                if i == 0:
                    grid[i][j] += grid[i][j-1]
                else:
                    grid[i][j] += min(grid[i-1][j],grid[i][j-1])
        return grid[-1][-1]
