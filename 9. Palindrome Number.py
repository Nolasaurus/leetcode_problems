class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        pal = False
        if x < 0:
            return False
        elif x == x % 10:
            return True
        else:
            xstr = str(x)
            for i in range(int(len(xstr)/2)):
                if xstr[i] == xstr[-1-i]:
                    pal = True
                else:
                    pal = False
                    break

        return pal

testCases = [121, 123123, 1000021]
testOutputs = [True, False, False]

tester = Solution()
iter = 0
for case in testCases:
    output = tester.isPalindrome(testCases[iter])
    print (output, 'SHOULD BE',testOutputs[iter])
    iter += 1