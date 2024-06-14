# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        s = ''
        if head is None:
            return
        temp = head
        while temp is not None:
            s = s + str(temp.val)
            temp = temp.next
        return int(s,2)