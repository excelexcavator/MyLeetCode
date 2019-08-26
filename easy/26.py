class Solution(object):
    def removeDuplicates(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        if not nums: return 0
        temp = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == temp:
                nums.pop(i)
            else:
                temp = nums[i]
        return len(nums)
