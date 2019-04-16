# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list[float]:
        if not root:
            return None
        c,r=[root],[]
        while c:
            r.append([p.val for p in c])
            c = [child for node in c for child in (node.left,node.right) if child]
        result = []
        for i in r:
            result.append(sum(i)/len(i))
        return result