# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):

        ##remove root from LLs
        curr = dummy = ListNode()
        while list1 and list2:

            if list1.val < list2.val: #compare and put smaller value in list
                curr.next = list1 #set curr pointer to list1
                list1, curr = list1.next, list1 # move first list1 element to curr, 
                                                # move down list1 to next node

            else:
                curr.next = list2 #if val2 >= list1
                list2, curr = list2.next, list2 #move first list2 element to curr,
                                                #move down list2 to next node

        if list1 or list2: #if there are any more elements
            if list1:
                curr.next = list1
            else: 
                curr.next = list2

        return dummy.next

tester = Solution()

cases = [[1,7,3,6,5,6],[1,2,3], [2,1,-1], ]
corr = [3, -1, 0]

for i, case in enumerate(cases):
    out = tester.reverseList(case)
    print(out, (out==corr[i])*"Correct")