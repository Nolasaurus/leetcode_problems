class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
    def append(self, new_node):
        current = self.val
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

tester = Solution()
case = [1,2,3,4,5,6]
e1 = Node(case[0])
l1 = LinkedList(e1)

for i in range(1,len(case)-1):
    l1.append(Node(i))

print(tester.middleNode(l1))

"""
>>> 3/2
1.5
>>> 3//2 # floor
1
>>> -(-3//2) # ceil
2

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.



 Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

"""


