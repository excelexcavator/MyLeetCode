class Solution(object):
    def maxSubArray(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        maxsum = -float('inf')
        tempsum = 0
        for i in range(len(nums)):
            tempsum += nums[i]
            if tempsum > maxsum:
                maxsum = tempsum
            if tempsum < 0:
                tempsum = 0
        return maxsum
