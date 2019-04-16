class Solution:
    """
    用状态机来判断状态是否转换，若转换，进行对应的操作，
    注意开始和结束
    """
    def state(self, prices, i, sele, buy):
        if prices[i + 1] < prices[i]:
            self.STATE = 2
        if prices[i + 1] > prices[i]:
            self.STATE = 1
            buy.append(prices[i])

    def up(self, prices, i, sele, buy):
        if prices[i + 1] < prices[i]:
            self.STATE = 2
            sele.append(prices[i])

    def down(self, prices, i, sele, buy):
        if prices[i + 1] > prices[i]:
            self.STATE = 1
            buy.append(prices[i])

    def maxProfit(self, prices):
        buy = []
        sele = []
        begin = 0
        up = 1
        down = 2
        self.STATE = begin
        swithcher = {0: self.state, 1: self.up, 2: self.down}
        for i in range(len(prices) - 1):
            swithcher.get(self.STATE)(prices, i, sele, buy)
        if len(sele) != len(buy):
            sele.append(prices[-1])
        porfit = sum(sele) - sum(buy)

        return porfit

    """
    方法二：看的别人的。最利润，就是所有升序的最大值与最小值的差之和  
    """

    def maxProfit2(self, prices):
        porfit = 0
        for i in range(len(prices)-1):
            if prices[i] < prices[i+1]:
                porfit = porfit + prices[i+1] - prices[i]
        return porfit

    
s = Solution()
print(s.maxProfit2([7,1,5,3,6,4]))
