class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if len(s) == 0:
            return True

        for i, letter in enumerate(s):
            if letter not in t:
                return False
            else:
                #truncate t to just after where you found the letter (delete letter)
                t = t[t.find(letter)+1:]

        return True

tester = Solution()
s = ["bb", "ab", "acb","abc", "axc", "acd"]
t = ["ahbgdc", "baab", "ahbgdc", "ahbgdc","ahbgdc", "bbbbbabbbbbcbbbbbd"]
corr = [False, True, False, True, False, True, True]

for i, case in enumerate(s):
    out = tester.isSubsequence(s[i], t[i])
    print(out, (out==corr[i])*"Correct")

'''
def isSubsequence(self, s, t):
    for c in s: for every s letter
        i = t.find(c) search t for letter
        if i == -1: not in? return False
            return False
        else: shorten list.
            t = t[i+1:]
    return True
'''