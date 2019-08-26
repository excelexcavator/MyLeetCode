class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
            :type s: str
            :rtype: int
            """
        idx = 0
        lmax = 0
        buf = ""
        while idx < len(s):
            if s[idx] in buf:
                lmax = max(lmax,len(buf))
                buf = buf[(buf.index(s[idx]))+1:] + s[idx]
            else:
                buf += s[idx]
            idx += 1
    return max(lmax, len(buf))
