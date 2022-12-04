class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        #label every letter with unique id
        #compare two lists
        #if same list, return true
        if len(s) != len(t):
            return False

        id1 = {}
        id2 = {}

        for i, letter  in enumerate(s):
            if s[i] not in id1.keys():
                id1[letter] = i #assign key and value {letter: "id"}

            if t[i] not in id2.keys():
                id2[t[i]] = i #assign key and value {letter: "id"}

            if id2[t[i]] != id1[s[i]]:
                return False
        return True

tester = Solution()

word1 = ["baba", "bbbaaaba", "egg", "foo", "paper"]
word2 = ["badc", "aaabbbba", "add", "bar", "title"]
corr = [False, False, True, False, True]

for i, case in enumerate(word1):
    out = tester.isIsomorphic(word1[i], word2[i])
    print(out, (out==corr[i])*"Correct")
