# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(self, head, left, right):
    count = 0
    
    prev = ListNode(0)
    prev.next = head
    curr = prev
    
    while curr:



# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
    
           