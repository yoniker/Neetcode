# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #iterative solution will use a result list, as well as a stack of nodes
        treeNodesToVisit = []
        ans = []
        while root or len(treeNodesToVisit)>0:
            if root:
                if root.left:
                    treeNodesToVisit.append(root) #add to the stack current root, and visit its left subtree
                    root = root.left
                else: #no left subtree- I can visit the node right now,and its right subtree
                    ans.append(root.val)
                    root=root.right
            else:
                root = treeNodesToVisit.pop(-1) #i pop a node from the stack- those nodes had some left subtrees that i visited already
                ans.append(root.val)
                root=root.right
        return ans