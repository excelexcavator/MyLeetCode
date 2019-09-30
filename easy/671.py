# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findSecondMinimumValue(self, root):
        """
            :type root: TreeNode
            :rtype: int
            """
        minimum = root.val
        def findmini(node):
            if not node.left:
                return node.val
            else:
                l = findmini(node.left)
                r = findmini(node.right)
                if min(l,r) == minimum:
                    return max(l,r)
                else:
                    return min(l,r)
    
        result = findmini(root)
        if result != minimum:
            return result
        else:
            return -1
