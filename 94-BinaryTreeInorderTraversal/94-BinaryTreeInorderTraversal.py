# Last updated: 24/03/2026, 22:39:17
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Initialize an empty list to store the result
        result = []
        
        # Helper function to perform the inorder traversal
        def inorder(node):
            # Base case: if the node is None, return
            if not node:
                return
            # Traverse the left subtree
            inorder(node.left)
            # Visit the current node
            result.append(node.val)
            # Traverse the right subtree
            inorder(node.right)
        
        # Start the inorder traversal from the root
        inorder(root)
        
        # Return the final result
        return result