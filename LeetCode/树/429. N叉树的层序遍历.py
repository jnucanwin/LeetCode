
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

import queue


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        Q = queue.Queue()
        i = 0
        Q.put([root, i])
        result = []
        while not Q.empty():
            s = Q.get()
            p = s[0]
            j = s[1]
            if j > len(result) - 1:
                result.append([])
            result[j].append(p.val)
            for c in p.children:
                Q.put([c, j + 1])
        return result


b = Node(2,[])
c= Node(7,[])
d= Node(1,[])
a = Node(4,[b,c,d])

s = Solution()
print(s.levelOrder(a))