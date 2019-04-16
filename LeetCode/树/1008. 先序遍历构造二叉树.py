# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def bstFromPreorder(self, preorder) -> TreeNode:
        if len(preorder) == 0:
            return
        root = TreeNode(preorder[0])
        i = 1
        for i in range(1,len(preorder)):
            if preorder[0] < preorder[i]:
                break
        if i == len(preorder)-1 and preorder[i] < preorder[0]:
            i += 1

        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root

s = Solution()
s.bstFromPreorder([8,5,1,7,10,12])

