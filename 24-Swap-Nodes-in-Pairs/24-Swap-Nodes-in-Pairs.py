# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        count = 0
        last =current

        while current:
            count = count + 1
            if count ==1 and head.next!=None:
                head = current.next
                tmp = None
            if last.next !=None and count%2==0:
                
                last.next =current.next
                current.next= last
                if tmp!=None:
                    tmp.next =current

                print(current.next)

                current = current.next
                tmp = current
               

                
            
            last = current
            current = current.next

        return head