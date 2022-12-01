class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower()
        half = int(len(s)/2)
        vowels = list("aeiou")

        s1_ct = 0

        for i in range(half):
            if s[i] in vowels:
                s1_ct += 1
            if s[half+i] in vowels:
                s1_ct -= 1

        return s1_ct == 0



    
tester = Solution()

cases = ["book", "textbook"]

for i in range(len(cases)):
    print(tester.halvesAreAlike(cases[i]))