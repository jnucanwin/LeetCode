# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root and(not root.left and not root.right):
            return None
        r = root.right
        l = root.left
        # root.left = r
        # root.right = l
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(r)
        return root

a = TreeNode(4)
b = TreeNode(2)
c= TreeNode(7)
d= TreeNode(1)
e = TreeNode(3)
f= TreeNode(6)
g = TreeNode(5)
h = TreeNode(9)

a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = h
s = Solution()
s.invertTree(a)
from 树.traverse import LevelOrder
LevelOrder(a)