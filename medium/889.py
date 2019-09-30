# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
            :type pre: List[int]
            :type post: List[int]
            :rtype: TreeNode
            """
        i = len(pre)
        node = TreeNode(pre[0])
        if i == 1:
            return node
        else:
            while set(pre[1:i-1]) != set(post[:i-2]):
                i -= 1
            if i == 2:
                node.left = self.constructFromPrePost(pre[1:],post[:-1])
            else:
                node.left = self.constructFromPrePost(pre[1:i-1],post[:i-2])
                node.right = self.constructFromPrePost(pre[i-1:],post[i-2:-1])
            return node
