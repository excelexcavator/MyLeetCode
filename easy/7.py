class Solution(object):
    def reverse(self, x):
        """
            :type x: int
            :rtype: int
            """
        flag = 1
        if x < 0:
            flag = -1
            x *= flag
    
        y = 0
        while 1:
            temp = x % 10
            x = (x - temp) / 10
            y = y * 10 + temp
            if x == 0:
                break
        
        y *= flag
        if y < -2**31 or y > 2**31-1:
            return 0
        else:
        return y
