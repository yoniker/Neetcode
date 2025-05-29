# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def goLeftestNode(self,root): #returns a list of all the nodes in a path to the leftmost node
        path = []
        while root:
            path.append(root)
            root = root.left
        return path


    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None #minus infinity/throw
        currentNumVisitedNodes = 0
        #First, get the path and the leftmost node
        currentPath = self.goLeftestNode(root)
        while currentNumVisitedNodes < k and len(currentPath) >0:
            #visit current node - it is in the last element of the path
            currentNode = currentPath.pop(-1)
            currentNumVisitedNodes += 1
            if currentNode.right and currentNumVisitedNodes<k:
                currentPath = currentPath + self.goLeftestNode(currentNode.right)
            

        if k!=currentNumVisitedNodes:
            return None
        return currentNode.val
