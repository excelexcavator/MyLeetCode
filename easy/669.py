# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        """
            :type root: TreeNode
            :type L: int
            :type R: int
            :rtype: TreeNode
            """
        def trim(node):
            if not node:
                return None
            elif node.val<L:
                return trim(node.right)
            elif node.val>R:
                return trim(node.left)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node
        return trim(root)
