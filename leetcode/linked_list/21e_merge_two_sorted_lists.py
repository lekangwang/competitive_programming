# https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # setup
        head, tail = None, None
        p1, p2 = list1, list2

        while p1 != None or p2 != None:
            node_to_be_inserted = None
            # compare nodes
            if p1 == None: 
                node_to_be_inserted = p2
                p2 = p2.next
            elif p2 == None:
                node_to_be_inserted = p1
                p1 = p1.next
            else:
                if p1.val <= p2.val:
                    node_to_be_inserted = p1
                    p1 = p1.next
                else: 
                    node_to_be_inserted = p2
                    p2 = p2.next
            
            if tail == None:
                tail = node_to_be_inserted
                tail.next = None
                head = tail
            else:
                tail.next = node_to_be_inserted
                tail = tail.next
                tail.next = None
        return head
