class Solution(object):
    def strStr(self, haystack, needle):
        """
            :type haystack: str
            :type needle: str
            :rtype: int
            """
        l = len(needle)
        for idx in range(len(haystack)-l+1):
            if haystack[idx:idx+l] == needle:
                return idx
        return -1
