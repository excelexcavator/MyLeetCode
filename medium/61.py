# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
            :type head: ListNode
            :type k: int
            :rtype: ListNode
            """
        if not head: return head
        idx = head
        l = 1
        while idx.next:
            l += 1
            idx = idx.next
        if not k%l: return head
        idx = head
        for i in range(l-k%l-1):
            idx = idx.next
        temp = idx.next
        idx.next = None
        newhead = temp
        for i in range(k%l-1):
            temp = temp.next
        temp.next = head
        return newhead
