class Solution(object):
    def isPalindrome(self, x):
        """
            :type x: int
            :rtype: bool
            """
        if x < 0:
            return False
        y = 0
        val = x
        while x != 0:
            y = y * 10 + x % 10
            x = (x - x % 10) / 10
        
        if y == val:
            return True
        else:
        return False
