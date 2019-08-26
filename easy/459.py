class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
            :type s: str
            :rtype: bool
            """
        l = len(s)
        for i in range(1,l/2+1):
            if l%i == 0 and s[:i]*(l/i) == s: return True
        return False
