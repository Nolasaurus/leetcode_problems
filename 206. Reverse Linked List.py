# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        if not head or not head.next: #if 0 or 1 element list return head
            return head

        second = head.next #all of the LL except the first element
        reverse = self.reverseList(second) ##call function again with rest of list

        #second.next = head 
        #head.next = None
        
        return reverse

tester = Solution()

cases = [[1,7,3,6,5,6],[1,2,3], [2,1,-1], ]
corr = [3, -1, 0]

for i, case in enumerate(cases):
    out = tester.reverseList(case)
    print(out, (out==corr[i])*"Correct")