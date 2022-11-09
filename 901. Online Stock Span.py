import time
class StockSpanner(object):
    def __init__(self):
        self.lastPrice = []
        
    def next(self, price):

        span = 1
        while self.lastPrice and price >= self.lastPrice[-1][0]:
            span += self.lastPrice.pop()[1]

        self.lastPrice.append([price, span])
        return span



#testCase1 = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
#prices = [[],[31],[41],[48],[59],[79]]
prices = [[],[100],[80],[60],[70],[60],[75],[85]]
#prices = [[],[29],[91],[62],[76],[51]]
#prices = [[],[28],[14],[28],[35],[46],[53],[66],[80],[87],[88]]

testOutputs = ["",1,1,1,2,1,4,6]
#testOutputs = ["",1,2,3,4,5]
#testOutputs = ["",1,2,1,2,1]
#testOutputs = ["",1,1,3,4,5,6,7,8,9,10]
start = time.time()
tester = StockSpanner()
iter = 0
for price in prices:
    output = tester.next(prices[iter])
    print(output, testOutputs[iter], output == testOutputs[iter])
    iter += 1

print("elapsed: ", time.time()-start)