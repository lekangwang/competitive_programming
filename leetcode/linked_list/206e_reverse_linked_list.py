# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        p, c, n = None, head, None

        while c != None:
            # update next and previous
            n = c.next

            # point curr to prev
            c.next = p

            # update curr and prev
            p = c
            c = n
        
        return p
        