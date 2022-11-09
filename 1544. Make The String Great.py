class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        global Loops
        Loops = 0
        maxLoops = 50
        
        while (Loops < 10)*(s.isupper() != True) | (s.islower() != True):
            for i in range(len(s)):
                if i+1 < len(s):

                    if s[i].upper() == s[i+1].upper(): #same letter?
                        if (((s[i].isupper() != True) & (s[i+1].islower() != True)) | 
                            ((s[i].islower() != True) & (s[i+1].isupper() != True))):

                            s = s[:i] + s[i + 2:]
            Loops+=1
            if Loops > maxLoops:
                break
            
            if not s:
                break

            if (((s.isupper() == True) | (s.islower() == True))):
                break

        return s


testCases = ["leEeetcode", "abBAcC", "s", 'Pp', 'mC']
testOutputs = ["leetcode", "", "s", "", "mC"]

testWord = Solution()
i = 0
for case in testCases:
    output = testWord.makeGood(testCases[i])
    print (case, output, output==testOutputs[i], Loops)
    i += 1