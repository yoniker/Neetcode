# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        left_inorder = self.inorderTraversal(root=root.left)
        left_inorder.append(root.val)
        right_inorder = self.inorderTraversal(root=root.right)
        return left_inorder + right_inorder        
        