class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:


        


'''
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while 
preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
'''
tester = Solution()

word1 = ["egg", "foo", "paper"]
word2 = ["add", "bar", "title"]
corr = [True, False, True]

for i, case in enumerate(word1):
    out = tester.frequencySort(case)
    print(out, (out==corr[i])*"Correct")