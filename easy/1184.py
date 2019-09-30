class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
            :type distance: List[int]
            :type start: int
            :type destination: int
            :rtype: int
            """
        s = min(start, destination)
        d = max(start, destination)
        return min(sum(distance[s:d]), sum(distance)-sum(distance[s:d]))
