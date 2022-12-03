class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #close if Operation 1: Swap any two existing characters.
        #close if Transform every occurrence of one existing character into
        #another existing character, and do the same with the other character.

        n1 = len(word1)
        n2 = len(word2)
        list_unique1 = list(set(word1))
        list_unique2 = list(set(word2))

        split_word1 = list(word1)
        split_word2 = list(word2)

        if n2 != n1:
            return False

        for letter in list_unique1:
            if letter not in list_unique2:
                return False

        for letter in list_unique2:
            if letter not in list_unique1:
                return False

        ##count unique characters by character
        uniq_ct_2 = []
        uniq_ct_1 = []

        for i in list_unique1:
            uniq_ct_1.append(split_word1.count(i))

        for i in list_unique2:
            uniq_ct_2.append(split_word2.count(i))

                        ##sort characters
        if sorted(uniq_ct_1) == sorted(uniq_ct_2):  ## if unique count matches

            return True                 ## return true
        return False

tester = Solution()

word1 = ["uau","abc", "a", "cabbba", "abbzzca"]
word2 = ["ssx","bca", "aa", "abbccc", "babzzcz"]

corr = [False,True, False, True, False]

for i, case in enumerate(word1):
    out = tester.closeStrings(case, word2[i])
    print(out, (out==corr[i])*"Correct")