# https://leetcode.com/problems/middle-of-the-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find the # of nodes in the LL
        num_nodes = 0
        temp = head
        while temp != None:
            num_nodes += 1
            temp = temp.next
        
        # calculate nodes to skip
        nodes_to_skip = num_nodes // 2
        middle = head
        for i in range(nodes_to_skip):
            middle = middle.next
    
        return middle