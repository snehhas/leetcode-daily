# Last updated: 24/03/2026, 22:38:44
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h2=None
        while (head!=None):
            next_p=head.next
            head.next=h2
            h2=head
            head=next_p
        return h2