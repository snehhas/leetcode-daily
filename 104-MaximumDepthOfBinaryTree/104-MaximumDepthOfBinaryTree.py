# Last updated: 24/03/2026, 22:39:14
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        else:
            left=self.maxDepth(root.left)
            right=self.maxDepth(root.right)
            return max(left,right)+1
        