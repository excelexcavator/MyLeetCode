# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
        
        n1 = 0
        n2 = 0
        count = 1
        while 1:
            n1 += l1.val * (10 ** (count-1))
            count += 1
            if l1.next == None:
                break
            else:
                l1 = l1.next
        
        count = 1
        while 1:
            n2 += l2.val * (10 ** (count-1))
            count += 1
            if l2.next == None:
                break
            else:
                l2 = l2.next
    
        val = n1 + n2
        val_list = []
        while 1:
            temp = int(val % 10)
            val_list.append(temp)
            val -= temp
            val /= 10
            if val == 0:
                break

                    out = ListNode(None)
                    head = out
for i in range(len(val_list)):
    temp = ListNode(None)
    temp.val = val_list[len(val_list)-i-1]
    temp.next = head.next
        head.next = temp
        
        return out.next
