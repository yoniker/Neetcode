# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    # def height(self,root,stop_checking_height_at=None):
    #         if root is None: return 0
    #             return
    #         left_height = 1+self.height(root.left,stop_checking_height_at)
    #         if stop_checking_height_at and left_height>stop_checking_height_at:
    #             return left_height #The tree is too high for sure
    #         right_height = 1+self.height(root.right,stop_checking_height_at)
    #         return max(left_heigh,right_height)
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode],direct_comparison=False) -> bool:
        if root is None and subRoot is None:
            return True
        if (root and subRoot is None) or (subRoot and root is None):
            return False
        if root.val == subRoot.val:
            if self.isSubtree(root.left,subRoot.left,direct_comparison=True) and self.isSubtree(root.right,subRoot.right,direct_comparison=True):
                return True
        if direct_comparison:
            return False
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)

        