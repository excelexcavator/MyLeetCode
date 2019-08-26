class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
            :type nums1: List[int]
            :type nums2: List[int]
            :rtype: float
            """
        l = len(nums1) + len(nums2)
        idx = 0
        for i in nums2:
            flag = 0
            while idx < len(nums1):
                if nums1[idx] >= i:
                    nums1.insert(idx,i)
                    idx += 1
                    flag = 1
                    break
                idx += 1
            if flag == 0:
                nums1.append(i)
        #if len(nums1) > l/2:
        #    break
        if l % 2 == 0:
            return (nums1[l/2-1] + nums1[l/2])/2.0
else:
    return nums1[l/2]
