class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True
        val = root.val

        def dfs(root, val):
            if not root:
                return True
            if root.val != val:
                return False
            return dfs(root.left, val) and dfs(root.right, val)

        return dfs(root, val)
