class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        if current == None:
            return None
        while current.next!= None: 

            if current.val == current.next.val:
                current.next= current.next.next
            else:

                current = current.next
        return(head)

