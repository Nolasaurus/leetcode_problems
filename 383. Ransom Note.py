class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        print(ransomNote, magazine)

tester = Solution()

rNotes = ['a','aa', 'aa']
magz = ['b','ab', 'aab']
corr = [False, False, True]
for i in range(len(rNotes)):
    print(tester.canConstruct(rNotes[i], magz[i]))