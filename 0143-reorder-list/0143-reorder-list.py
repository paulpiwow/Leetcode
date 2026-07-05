# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        #find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #we're at the beginning of the second half, reverse second half
        second = slow.next
        prev = None
        slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        #now that the second half has been reversed, merge the two halves
        first = head
        second = prev   #prev is the new head of the second half of the list
        while second:
            tmp1 = first.next      # save rest of first half
            tmp2 = second.next     # save rest of second half
            first.next = second    # point to second's node
            second.next = tmp1     # stitch second's node to rest of first
            first = tmp1           # advance both pointers
            second = tmp2