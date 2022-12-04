class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        avg_diff = []
        left_side = 0
        right_side = sum(nums)
        
        for i in range(n):
            left_side = left_side + nums[i]
            right_side = right_side - nums[i]
            if i == 0:
                avg_diff.append(abs(nums[0]-right_side//(n-1)))
            else:
                if n-i-1 !=0:
                    avg_diff.append(abs(left_side//(i+1)-right_side//(n-i-1)))
        avg_diff.append(abs(sum(nums)//n))
        minavg = 10^99
        index = 0
        for i, number in enumerate(avg_diff):
            if number == 0:
                return i
            if number < minavg:
                minavg = number
                index = i


        if nums[0] < minavg:
            return 0
        elif nums[-1] <minavg:
            return n
        else:
            return index





        
        #print(avg_diff)
        #print(sorted(avg_diff, key = lambda x: x[1]))
        return sorted(avg_diff, key = lambda x: x[1])[0][0]


tester = Solution()
nums = [[4,2,0], [1,2,3,4,5],[1,1,1,1,1], [2,5,3,9,5,3], [0], [1,2,3]]

corr = [2,0,0,3,0,0]

for i, case in enumerate(nums):
    out = tester.minimumAverageDifference(case)
    print(out, (out==corr[i])*"Correct")