# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
        out = ListNode(0)
        idx = out
        while 1:
            if l1 == None:
                idx.next = l2
                break
            elif l2 == None:
                idx.next = l1
                break
            if l1.val <= l2.val:
                idx.next = l1
                idx = idx.next
                l1 = l1.next
            else:
                idx.next = l2
                idx = idx.next
                l2 = l2.next
        return out.next
