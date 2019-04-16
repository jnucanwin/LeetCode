class Solution:
    """
    A 排序，转负数，有剩余，则转最小的（98.55%）
    """
    def largestSumAfterKNegations(self, A:list, K: int):
        if K == 0:
            return sum(A)
        A.sort()
        flag = 0
        for i in range(len(A)):
            if A[i]< 0 and K > 0:
                flag = 1
                A[i] = -A[i]
                K -= 1
            else:
                break
        if K == 0:
            return sum(A)
        if flag == 1:
            A.sort()
        k = K % 2
        if k == 0:
            return sum(A)
        else:
            return sum(A) - 2*A[0]





s = Solution()
print(s.largestSumAfterKNegations([4,2,3],1))
