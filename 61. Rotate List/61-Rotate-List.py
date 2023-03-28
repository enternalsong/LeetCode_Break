# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return head
        current = head
        count = 0
        slist = []
        nodelist=[]
        print(ListNode(1))
        while current:
            slist.append(current.val)
            current = current.next  
        print(slist)
        rlist = slist
        k = k % len(rlist)
        for i in range(k):
            out = rlist[len(rlist)-1]
            rlist.insert(0,out)
            rlist.pop()
        print(rlist)
        for i in range(len(rlist)):
            if i ==0:
                savenode = ListNode(rlist[i])
                current = savenode
                
            else:
                current.next = ListNode(slist[i])
                current = current.next

        return(savenode)