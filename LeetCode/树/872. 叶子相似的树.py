# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def leafSimilar(self, root1: 'TreeNode', root2: 'TreeNode') -> 'bool':
        def getLeaf(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            return getLeaf(root.left) + getLeaf(root.right)

        return getLeaf(root1) == getLeaf(root2)


class Solution1:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def leaf(root):
            if not root:
                return []
            if not root.left and not root.right:
                return [root.val]
            res = []
            res += leaf(root.left)
            res += leaf(root.right)
            return res
        return leaf(root1) == leaf(root2)
a = TreeNode(1)
b = TreeNode(2)


a.left = b




s= Solution()
print(s.leafSimilar(a,b))
