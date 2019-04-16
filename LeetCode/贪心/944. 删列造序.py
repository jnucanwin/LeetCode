class Solution:
    """
    判断每一列，若该列不符合非降序，则count += 1
    """
    def minDeletionSize(self, A) -> int:
        count = 0
        for j in range(len(A[0])):
            for i in range(len(A)-1):
                if A[i][j]>A[i+1][j]:
                    count += 1
                    break
        return count

s = Solution()
print(s.minDeletionSize(["cba", "daf", "ghi"]))