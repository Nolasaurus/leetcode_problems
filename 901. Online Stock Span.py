class StockSpanner(object):

    def __init__(self):
        

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


testCases = [[2,7,11,15], [3,2,4], [3,3], [3,2,3]]
target = [9, 6, 6, 6]
testOutputs = [[0,1], [1,2], [0,1], [0,2]]

tester = Solution()
iter = 0
for case in testCases:
    output = tester.twoSum(testCases[iter], target[iter])
    print (output, testOutputs[iter])
    iter += 1