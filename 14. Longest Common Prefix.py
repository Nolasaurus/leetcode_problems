class Solution:
    def longestCommonPrefix(self, strs) -> str:
        shortest = min(strs)
        #shortest = strs[0]
        #for word in strs[1:]:
        #    if len(word) < len(shortest):
        #        shortest = word
            

        stack = []
        for i in range(len(shortest)): #for each letter
            stack.append(shortest[i])  #add the letter to the stack
            
            for word in strs:           #for each word in the input
                if word[i] == shortest[i]: #check if the letter in place i in the word is the same in both
                    pass                    #if so, leave the letter in the stack
                else:
                    stack.pop()             #otherwise, remove the letter and return the stack
                    return "".join(stack)

        return "".join(stack)  #leave the first letter if nothing else matches


words = [["cir","car"], ["flower", "floor", "flute"], ["ab","a"], [" ", "blue"]]
corr = ["c", "fl", "a", ""]
test = Solution()

for i in range(len(words)):
    print(test.longestCommonPrefix(words[i]), test.longestCommonPrefix(words[i])==corr[i])



""" better solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        m = max(strs) #get longest word in input
        n = min(strs) #get shortest word in input
        
        for i in range(len(n)): #for each letter in shortest word
            if m[i] != n[i]:    #if the corresponding letter in the short word doesn't match the long word
                return m[:i]    #return m up to the ith place (exclusive)
        return n 
"""
