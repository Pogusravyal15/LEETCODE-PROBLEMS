class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next=next
class solution:
    def middleNode(self, head: ListNode)->ListNode:
        count=0
        current=head
        while current:
            count+=1
            current=current.next
        current=head
        for i in range(count//2):
            current=current.next
        return current
