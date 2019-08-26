class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
            :type A: str
            :type B: str
            :rtype: int
            """
        la = len(A)
        lb = len(B)
        times = lb / la + (lb % la != 0)
        if B in A * times: return times
        times += 1
        if B in A * times: return times
        return -1
