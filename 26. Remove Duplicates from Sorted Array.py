class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:#
        stack = []
        for i in nums:
            if i not in stack:
                stack.append(i)
        nums = stack

        return len(stack)






case = [[0,0,1,1,1,2,2,3,3,4],[1,1,2]]
corr = [5, 2]
test = Solution()

for i in range(len(case)):
    print(test.removeDuplicates(case[i]), test.removeDuplicates(case[i])==corr[i])
