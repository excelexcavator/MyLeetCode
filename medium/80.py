class Solution(object):
    def removeDuplicates(self, nums):
        """
            :type nums: List[int]
            :rtype: int
            """
        if not nums: return 0
        temp = nums[len(nums)-1]
        flag = 0 # the same number has only appeared for once
        for i in range(len(nums)-2,-1,-1):
            if nums[i] == temp and not flag:
                flag += 1
            elif nums[i] == temp and flag:
                nums.pop(i)
            else:
                temp = nums[i]
                flag = 0
        return len(nums)

