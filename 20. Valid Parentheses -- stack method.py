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
        stack = []
        dict = {'(':')','[':']','{':'}'}

        
        if len(s)%2 != 0:
            return False

        for i in s:
            if i in dict.keys(): ## is i a left bracket? do so until there are no more left brackets
                stack.append(i)  ## then add it to the stack
            else:                ## otherwise (i is a right bracket)
                if len(stack) == 0: ## and there's nothing in the stack...
                    return False    ## invalid parens
                a = stack.pop()     ## look at the last bracket in stack
                if i != dict[a]:    ##if it doesn't match the corresp. closing bracket
                    return False    ## invalid parens
        
        if len(stack)>0: ## if you've done the above for the whole list and there's still brackets...
            return False ## they're not valid
        
        ## you've gone through the whole list and not found any invalid
        return True


test = Solution()
testcases = ["()","()[]{}","(]", ")))", "([)]", "(){}}{", "(([]){})"]
for case in testcases:
    print(test.isValid(case))