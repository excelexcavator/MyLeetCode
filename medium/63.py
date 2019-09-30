class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
            :type obstacleGrid: List[List[int]]
            :rtype: int
            """
        n,m = len(obstacleGrid), len(obstacleGrid[0])
        grid = map(lambda x:map(lambda y:int(not y), x), obstacleGrid)
        for i in range(m-1):
            if grid[0][i] == 0:
                grid[0][i+1] = 0
        for j in range(n-1):
            if grid[j][0] == 0:
                grid[j+1][0] = 0
        for i in range(1,m):
            for j in range(1,n):
                if not grid[j][i]:
                    continue
                grid[j][i] = grid[j][i-1]+grid[j-1][i]
        return grid[-1][-1]
