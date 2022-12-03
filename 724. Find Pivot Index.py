class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        '''Attempt 1 - too slow
        for i in range(len(nums)):
            if sum(nums[:i])==sum(nums[i+1:]):
                return i
        return -1
        '''

        #### recursion???
        ##TODO implement faster approach
        ## pick center spot
        n = len(nums)

        half = n//2 #floor 13->6.5->6
        sqrt_n = n**0.5

        if sum(nums[1:]) == 0:
            return 0
        if sum(nums[:-1]) == 0:
            return n

        for i in range(0,int(sqrt_n)):
            print(i)

        return -1

tester = Solution()

cases = [[1,7,3,6,5,6],[1,2,3], [2,1,-1], ]
corr = [3, -1, 0]

for i, case in enumerate(cases):
    out = tester.pivotIndex(case)
    print(out, (out==corr[i])*"Correct")


'''
Given an array of integers nums, calculate the pivot index
 of this array.

The pivot index is the index where the sum of all
 the numbers strictly to the left of the index is equal
  to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array,
 then the left sum is 0 because there are no elements
  to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists,
 return -1.

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
'''