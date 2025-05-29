# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:


    def isValidBST(self, root: Optional[TreeNode],min_value=None,max_value=None) -> bool:
        if root is None:
            return True
        if min_value and root.val<=min_value:
            return False
        if max_value and root.val>=max_value:
            return False
        if root.left and root.left.val>=root.val:
            return False
        if root.right and root.right.val<=root.val:
            return False
        if not self.isValidBST(root.left,min_value,root.val): #notice that if root.val<max then i broke the rule right here actually.
            return False
        return self.isValidBST(root.right,root.val,max_value) #same thing here, if this root's val is smaller than min, then by definition i wouldn't even be here