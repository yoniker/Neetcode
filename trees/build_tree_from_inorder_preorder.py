# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTreeWithHashmap(self, preorder: List[int], inorder: List[int],indices_hashmap,currentSkew) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) ==0 :
            return None
        if len(preorder)==1 or len(inorder) == 1:
            return TreeNode(val=preorder[0])
        root_value = preorder[0]
        index_root_value = indices_hashmap.get(root_value,None)
        if index_root_value is None:
            return None #illegal input, i can throw some exception?
        index_root_value -= currentSkew
        #index_root_value is exactly the same as number of elements in Left subtree
        left_inorder = inorder[:index_root_value]
        left_preorder = preorder[1:index_root_value+1]
        right_inorder = inorder[index_root_value+1:]
        right_preorder = preorder[index_root_value+1:]
        left_subtree = self.buildTreeWithHashmap(preorder=left_preorder,inorder=left_inorder,indices_hashmap=indices_hashmap,currentSkew=currentSkew)
        right_subtree = self.buildTreeWithHashmap(preorder=right_preorder,inorder=right_inorder,indices_hashmap=indices_hashmap,currentSkew = currentSkew+index_root_value+1)
        root = TreeNode(val=root_value,left=left_subtree,right=right_subtree)
        return root


    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0 or len(inorder) ==0 :
            return None
        if len(preorder)==1 or len(inorder) == 1:
            return TreeNode(val=preorder[0])
        hashmapped_indices = dict()
        for index,value in enumerate(inorder):
            hashmapped_indices[value] = index
        return self.buildTreeWithHashmap(preorder,inorder,indices_hashmap=hashmapped_indices,currentSkew=0)
        
        
        