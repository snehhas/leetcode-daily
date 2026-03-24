# Last updated: 24/03/2026, 22:39:16
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        ans=[]
        q=deque()
        q.append(root)

        while q:
            size=len(q)
            level=[]
            for i in range(size):
                curr_val=q.popleft()
                if curr_val:
                    q.append(curr_val.left)
                    q.append(curr_val.right)
                    level.append(curr_val.val)
            if level:
                ans.append(level)
        return ans
        