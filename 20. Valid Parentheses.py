"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        br = ["()", "[]", "{}"]

        n = len(s)
        if n%2 != 0:
            return False

        i = 0
        while s:
            if s in br:
                return True
            
            if len(s)==2 and s not in br:
                return False
            
            if i > len(s)-2:
                return False

            pair = s[i]+s[i+1]
            if pair in br:
                s = s[:i] + s[i + 2:]
                i = 0
            else:
                i+=1

        return True

        

test = Solution()
#testcases = ["(([]){})"]
testcases = ["()","()[]{}","(]", ")))", "([)]", "(){}}{", "(([]){})"]
for case in testcases:
    print(test.isValid(case))

        