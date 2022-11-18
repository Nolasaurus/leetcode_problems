'''
Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).
'''

class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        
        amt_decr = 0
        for i in range(len(nums)-3):
            print(nums[i], nums[i+1], nums[i+2])
            if nums[i+1] <= nums[i]:
                amt_decr += 1
            
            if nums[i+2] <= nums[i]:
                amt_decr += 1
            if nums[i+3] <= nums[i]:
                amt_decr += 1

        if nums[-2] >= nums[-1]:
            amt_decr +=1
            
        if amt_decr <2:
            return True
        else: return False
    
    ## Go through list of numbers
    ## count how many of the next two numbers (i+1, i+2) are less than or equal to i
    ## add up sum -> if >1, return false
    

test = Solution()
cases = [[1,2,10,5,7], [2,3,1,2], [1,1,1], [6,562,624,803,747,981,841]]
for case in cases:
    print(test.canBeIncreasing(case))