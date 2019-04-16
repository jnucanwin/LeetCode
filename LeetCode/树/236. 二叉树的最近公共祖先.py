# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import copy


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p1: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        s = []
        p_s = []
        q_s = []
        r = None
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
                    if p.val == p1.val:
                        p_s = copy.copy(s)
                    if p.val == q.val:
                        q_s = copy.copy(s)
                    if len(p_s) and len(q_s):
                        break
                    s.pop()
                    r = p
                    p = None
        for i in range(min(len(p_s),len(q_s))):
            if p_s[i] != q_s[i]:
                break
        if p_s[i] == q_s[i]:
            return p_s[i]
        else:
            return p_s[i-1]
n = []
for i in range(-1,3):
    n.append(TreeNode(i))
for i in range(0,3):
    n[i].left = n[i+1]
# a = TreeNode(1)
# b = TreeNode(2)
# c= TreeNode(8)
# d= TreeNode(0)
# e = TreeNode(4)
# f= TreeNode(7)
# g = TreeNode(9)
# h = TreeNode(3)
# i = TreeNode(5)

# a.left = b
# a.right = c
# b.left = d
# b.right = e
# c.left = f
# c.right = g
# e.left = h
# e.right = i
p = n[0]
while p.left:
    p = p.left
print(p.val)
s= Solution()
print(s.lowestCommonAncestor(n[0],n[-1],n[-2]).val)
