class Solution:
    def middleNode(self, head: ListNode) -> ListNode:

        LL_values = []
        count = 1
        while head and head.next:
            val = head.val
            count +=1
            LL_values.append(val) ##store head value
            ## point head to next node
            head = head.next

        middle = count//2 #floor

        ##rebuild list up to the middle node

        new_node = ListNode()
        dummy = ListNode()
        print(LL_values)

        while len(LL_values) > middle:
            
            new_node.next = head
            
            new_node.val = LL_values[-1]
            dummy = ListNode(head.val)
            
            LL_values = LL_values[:-1]
            dummy.next = head.next

            head = ListNode(new_node.val)
            head.next = new_node.next
            
                
        return head