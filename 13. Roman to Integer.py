class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        valueDict = {}
        valueDict['I'] = 1
        valueDict['V'] = 5
        valueDict['X'] = 10
        valueDict['L'] = 50
        valueDict['C'] = 100
        valueDict['D'] = 500
        valueDict['M'] = 1000


        romNum = [*s]
        arabNum = []

        # convert alpha to numeric
        for letter in romNum:
            arabNum.append(valueDict[letter])
        
        ans = 0
        addFlag = True
        for i in range(len(arabNum)-1):
            if arabNum[i] >= arabNum[i+1]:
                ans += arabNum[i]
                addFlag = True
            else:
                addFlag = False
                ans-= arabNum[i]
                
        ans += arabNum[-1]
        return ans




testcase = ["III", "IV", "MM", "MXM", "MIM", "MCMXCIV"]
testOutputs = [3, 4, 2000, 1990, 1999, 1994]


tester = Solution()
iter = 0
for str in testcase:
    output = tester.romanToInt(str)
    print(output, testOutputs[iter], output == testOutputs[iter])
    iter += 1