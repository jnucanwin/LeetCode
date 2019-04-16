
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        result = [0]
        for c in root.children:
            result += [self.maxDepth(c)]
        return max(result)+1