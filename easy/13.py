class Solution(object):
    def romanToInt(self, s):
        """
            :type s: str
            :rtype: int
            """
        V = 0
        i = 0
        while i < len(s):
            if s[i] == 'I':
                if i == len(s) - 1:
                    V += 1
                elif s[i+1] == 'V':
                    V += 4
                    i += 1
                elif s[i+1] == 'X':
                    V += 9
                    i += 1
                else:
                    V += 1
            elif s[i] == 'V':
                V += 5
            elif s[i] == 'X':
                if i == len(s) - 1:
                    V += 10
                elif s[i+1] == 'L':
                    V += 40
                    i += 1
                elif s[i+1] == 'C':
                    V += 90
                    i += 1
                else:
                    V += 10
            elif s[i] == 'L':
                V += 50
            elif s[i] == 'C':
                if i == len(s) - 1:
                    V += 100
                elif s[i+1] == 'D':
                    V += 400
                    i += 1
                elif s[i+1] == 'M':
                    V += 900
                    i += 1
                else:
                    V += 100
            elif s[i] == 'D':
                V += 500
            elif s[i] == 'M':
                V += 1000
            i += 1
        
        return V
