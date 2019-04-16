class Solution(object):
    def findContentChildren(self, g, s):
        """
        胃口饼干排序，用最小的饼干满足相应孩子。
        """
        i = 0
        j = 0
        count = 0
        g.sort()
        s.sort()
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return count