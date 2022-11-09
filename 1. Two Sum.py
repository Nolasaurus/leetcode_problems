class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        
        found = False

        while found == False:
            currNum = nums[-1]
            ix = 0
            gx = 0
            for i in nums[:-1]:
                if currNum + i == target:
                    indices = [ix, len(nums)-1]
                    found = True
                ix+=1
            gx+=1
            nums.pop() #partial list is done
        return indices


testCases = [[2,7,11,15], [3,2,4], [3,3], [3,2,3]]
target = [9, 6, 6, 6]
testOutputs = [[0,1], [1,2], [0,1], [0,2]]

tester = Solution()
iter = 0
for case in testCases:
    output = tester.twoSum(testCases[iter], target[iter])
    print (output, testOutputs[iter])
    iter += 1