class Solution(object):
    def longestCommonPrefix(self, strs):
        """
            :type strs: List[str]
            :rtype: str
            """
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]
        lmin = len(min(strs, key=len))
        if lmin == 0:
            return ""
        
        for i in range(lmin):
            flag = 0
            ch = strs[0][i]
            for j in range(1,len(strs)):
                if ch != strs[j][i]:
                    flag = 1
                    break
            if flag:
                break
        
        if not flag:
            return min(strs, key=len)
        elif i > 1:
            return strs[0][:i]
        elif i == 1:
            return strs[0][0]
        else:
            return ""
