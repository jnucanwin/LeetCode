class Solution:
    def partitionLabels(self, S: str) -> [int]:
        """
        从第一个字母开始，在字符串中从右往左寻找到第一个一样的
        遍历此区间，并且维持右端点，及找到一个划分（71.61%）
        注：字符串的划分为问题，经常用到维持区间这种方法。
        """
        i = 0
        ans = []
        while i < len(S):
            j = S.rfind(S[i])
            m = j
            k = i + 1
            while k < m:
                m = max(m, S.rfind(S[k]))
                k += 1
            m += 1
            ans.append(m - i)
            i = m
        return ans

s = Solution()
print(s.partitionLabels("aaababbccc"))