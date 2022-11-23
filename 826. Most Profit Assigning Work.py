class Solution:
    def maxProfitAssignment(self, difficulty: list[int], profit: list[int], worker: list[int]) -> int:
        maxP = 0
        #go through workers
        #select most profitable job with difficulty less than worker ability

        for i in range(len(worker)):
            if worker[i]>difficulty[i]:
                print(profit)

            
            

        return maxP




difficulty = [85,47,57]
profit = [24,66,99]
worker = [40,25,25]


corr = 0
test = Solution()
print(test.maxProfitAssignment(difficulty,profit,worker))
#for i in range(len(case)):
 #   print(test.removeDuplicates(case[i]), test.removeDuplicates(case[i])==corr[i])