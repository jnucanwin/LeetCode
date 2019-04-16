"""
# # Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if not root:
            return
        if len(root.children) == 0:
            return [root.val]
        result = []
        for c in root.childre:
            result.append[self.postorder(c.childre)]
        return result


