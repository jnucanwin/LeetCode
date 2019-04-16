# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def bst(root):
            if not root:
                return []
            res = []
            res += bst(root.left)
            res += [root]
            res += bst(root.right)
            return res
        res = bst(root)
        for i in range(0,len(res)-1):
            res[i].left = None
            res[i].right = res[i+1]
        res[-1].left = None
        res[-1].right = None
        return res[0]