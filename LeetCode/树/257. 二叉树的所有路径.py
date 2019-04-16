class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        s = []
        result = []
        r = None
        if not root:
            return []
        p = root
        while p or s:
            if p:
                s.append(p)
                p = p.left
            else:
                p = s[-1]
                if p.right and p.right != r:
                    p = p.right
                    s.append(p)
                    p = p.left
                else:
                    p = s[-1]
                    if not p.left and not p.right:
                        result.append([node.val for node in s])
                    p = s.pop()
                    r = p
                    p = None
        res = []
        for r in result:
            temp = ""
            for p in r:
                temp = temp + str(p) + "->"
            res.append(temp[:-2])
        return res
a = TreeNode(1)
b = TreeNode(2)
c= TreeNode(3)
d= TreeNode(5)
# e = TreeNode(4)
# f= TreeNode(7)
# g = TreeNode(9)
# h = TreeNode(3)
# i = TreeNode(5)

a.left = b
a.right = c
b.right = d

s = Solution()
s.binaryTreePaths(a)