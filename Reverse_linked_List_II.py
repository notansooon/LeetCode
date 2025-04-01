# Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

# Needs review

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseBetween(self, head, left, right):
    
    
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    pos = 1
    
    while prev and pos < left:
        prev = prev.next
        pox += 1

    curr = prev.next
    while curr and pos < right - left:
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
        pos += 1
# Input: head = [1,2,3,4,5], left = 2, right = 4
# Output: [1,4,3,2,5]
    
    
# Input: head = [1,2,3,4,5], left = 2, right = 3
# Output: [1,3,2,4,5]
    
           