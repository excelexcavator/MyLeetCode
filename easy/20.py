class Solution(object):
    def isValid(self, s):
        """
            :type s: str
            :rtype: bool
            """
        stack = []
        d = {'(':+1, ')':-1,
             '[':+2, ']':-2,
             '{':+3, '}':-3}
        for i in s:
            if d[i] > 0:
                stack.append(d[i])
            elif len(stack) == 0 or d[i] + stack.pop() != 0:
                return False
        if len(stack) == 0:
            return True
        else:
        return False
