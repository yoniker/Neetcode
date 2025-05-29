# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #I search for 'both' p and q. The first node for which I would turn in a different direction,is the answer, or if I found one of p or q
        while root.val!=p.val and root.val!=q.val:
            #Let's find out the direction based on p
            direction_for_p = root.left if p.val<root.val else root.right
            direction_for_q = root.left if q.val<root.val else root.right
            if direction_for_p!=direction_for_q:
                return root
            root = direction_for_p
        return root

        