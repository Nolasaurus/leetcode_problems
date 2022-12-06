# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
            
        even_head = head.next
        last_odd = cur = head
        
        i = 1
        while cur and cur.next:
            i+=1
            next_pointer = cur.next #hold pointer
            cur.next = cur.next.next #change pointer to next pointer, i.e. skip the next node
            cur = next_pointer #set next pointer
            if i%2 != 0:
                last_odd = cur #store pointer of last odd node
     
        last_odd.next = even_head #point last odd node to evenHead
        return head