class Solution:
    """
    将第一列全部转换为1
    除第一列外，将每一列转换为：1的个数大于0的个数(83.64%)
    注意：二进制化为十进制： int(x,2)
    """
    def matrixScore(self, A:[[int]]) -> int:
        for i in range(len(A)):
            if A[i][0] == 0:
                for j in range(len(A[0])):
                    A[i][j] =  abs(A[i][j] -1)

        for j in range(len(A[0])):
            count_0 = 0
            count_1 = 0
            for i in range(len(A)):
                if A[i][j] == 0:
                    count_0 += 1
                else:
                    count_1 += 1

            if count_0 > count_1:
                for i in range(len(A)):
                    A[i][j] =  abs(A[i][j] -1)
        sum = 0
        for num in A:
            n = ""
            for i in num:
                n = n + str(i)
            sum += int(n,2)
        return sum
s = Solution()
print(s.matrixScore([[1,0,1,0,],
                     [0,1,0,1],
                     [1,1,1,1],
                     [0,0,1,1]]))