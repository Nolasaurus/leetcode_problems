class Solution:
    def frequencySort(self, s: str) -> str:

        cts_dict = dict()
        for pair in [ (i,s.count(i)) for i in set(s) ]: #count occurrence of each character
            cts_dict[pair[0]] = pair[1]                 #put in dict

        #sort by occurrence
        cts_dict = dict(sorted(cts_dict.items(), key=lambda item: item[1], reverse=True))

        output = []
        #go through dict
        #add letter * # of occurrences to output str
        #
        for key in cts_dict:
            output.append(key*cts_dict[key])

        #join list into str
        return "".join(output)

tester = Solution()

cases = ["tree", "eeeeeeeeajsj", "cba"]
corr = [3, -1, 0]

for i, case in enumerate(cases):
    out = tester.frequencySort(case)
    print(out, (out==corr[i])*"Correct")