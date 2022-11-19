'''
Given a 0-indexed integer array nums, return true if it can be made strictly increasing after removing exactly one element, or false otherwise. If the array is already strictly increasing, return true.

The array nums is strictly increasing if nums[i - 1] < nums[i] for each index (1 <= i < nums.length).
'''

class Solution:
    def canBeIncreasing(self, nums: list[int]) -> bool:
        amt_dec = 0
        ix = 0
        n = len(nums)
        

        for i in range(n-1):
            if nums[i] >= nums[i+1]:
                ix = i
                amt_dec += 1
        
        if amt_dec==0:
            return True


        if amt_dec == 1:
            if ix == 0 or ix == n-2: ## first or next to last (remove first or remove last)
                return True
            if nums[ix-1] < nums[ix+1] or (ix+2 < n and nums[ix] < nums[ix+2]):
                return True
            
        return False

test = Solution()
cases = [[1,2,10,5,7], [2,3,1,2], [1,1,1], [6,562,624,803,747,981,841], [13,205,553,527,790,238]]
for case in cases:
    print(test.canBeIncreasing(case))