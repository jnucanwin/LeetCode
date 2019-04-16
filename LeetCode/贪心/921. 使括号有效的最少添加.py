class Solution:
    """
    使用栈进行配对。
    若栈空或者左括号，进栈
    若有括号并且栈顶为左括号，出栈
    返回栈的长度（76.77%）
    注：符号配对等问题，经常用到栈
    """
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for s in S:
            if len(stack) == 0:
                stack.append(s)
                continue
            if (s == ")" and stack[-1] == "(" ):
                stack.pop()
            else:
                stack.append(s)
        return len(stack)
s = Solution()
print(s.minAddToMakeValid("(((()"))