class Solution:
    """
    通过维持5元零钱和10元零钱数量来判断是否能继续进行下去
    """
    def lemonadeChange(self, bills) -> bool:
        c_5 = 0
        c_10 = 0
        for b in bills:
            if b == 5:
                c_5 += 1
            if b == 10:
                c_5 -= 1
                c_10 += 1
            if b == 20:
                if c_10 > 0:
                    c_10 -= 1
                    c_5 -= 1
                else:
                    c_5 -= 3
            if c_5 < 0 or c_10 < 0:
                return False
        return True


s = Solution()
print(s.lemonadeChange([5,5,10,10]))