# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            root = self.searchBST(root.left,val)
        else:
            root = self.searchBST(root.right,val)
        return root

a = TreeNode(4)
b = TreeNode(2)
c= TreeNode(7)
d= TreeNode(1)
e = TreeNode(3)
# f= TreeNode(6)
# g = TreeNode(5)
# h = TreeNode(9)

a.left = b
a.right = c
b.left = d
b.right = e
# c.left = f
# c.right = h
s = Solution()
print(s.searchBST(a,2))
# from 树.traverse import LevelOrder
# LevelOrder(a)