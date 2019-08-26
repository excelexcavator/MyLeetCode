class Solution(object):
    def isMonotonic(self, A):
        """
            :type A: List[int]
            :rtype: bool
            """
        temp = A[0]
        flag = 0
        out = True
        for i in range(1,len(A)):
            if flag == 0:
                if A[i] > temp:
                    flag = 1
                    temp = A[i]
                elif A[i] < temp:
                    flag = -1
                    temp = A[i]
            elif flag > 0:
                if A[i] > temp:
                    temp = A[i]
                elif A[i] < temp:
                    out = False
                    break
            else:
                if A[i] < temp:
                    temp = A[i]
                elif A[i] > temp:
                    out =False
                    break
    return out
