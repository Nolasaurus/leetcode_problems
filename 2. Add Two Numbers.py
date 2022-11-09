# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return "ListNode(val=" + str(self.val) + ", next={" + str(self.next) + "})"



def list_to_LL(arr):
    if len(arr) < 1:
        return None

    if len(arr) == 1:
        return ListNode(arr[0])
        
    return ListNode(arr[0], next=list_to_LL(arr[1:]))




def reverseList(head: ListNode) -> ListNode:
    prev = None
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return prev




def LL_to_list(LL: ListNode):
    list_out = []
    while LL:
        list_out.append(LL.val)
        LL = LL.next

    return list_out        
    

'''
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        #convert to list to number value
        l1_val = 0
        l2_val = 0

        list1 = LL_to_list(l1)
        list2 = LL_to_list(l2)

        for ix in range(len(list1)):
            l1_val += list1[ix]*10**ix
        

        for jx in range(len(list2)):
            l2_val += list2[jx]*10**jx

        total = str(l1_val+l2_val)
        out = []
        for kx in total[::-1]:
            out.append(int(kx))

        return list_to_LL(out)
        

testCase1_l1 = list_to_LL([2,4,3])
testCase1_l2 = list_to_LL([5,6,4])

testCase2_l1 = list_to_LL([0])
testCase2_l2 = list_to_LL([0])

testCase3_l1 = list_to_LL([9,9,9,9,9,9,9])
testCase3_l2 = list_to_LL([9,9,9,9])

testOutput1 = list_to_LL([7,0,8])
testOutput2 = list_to_LL([0])
testOutput3 = list_to_LL([8,9,9,9,0,0,0,1])

tester = Solution()

output = tester.addTwoNumbers(testCase1_l1, testCase1_l2)
print (output, '\n', 'SHOULD BE',testOutput1, '\n')

output = tester.addTwoNumbers(testCase2_l1, testCase2_l2)
print (output, '\n', 'SHOULD BE',testOutput2, '\n')

output = tester.addTwoNumbers(testCase3_l1, testCase3_l2)
print (output, '\n',  'SHOULD BE',testOutput3)

