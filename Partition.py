# Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

# You should preserve the original relative order of the nodes in each of the two partitions.




class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def solution(self, head, x):
    
    
    dummy = ListNode(0)
    dummy.next = head
    curr = dummy

    empty_list = []

    # Traverse and collect nodes >= x
    while curr.next:
        if curr.next.val >= x:
            empty_list.append(curr.next)  # store the node, not just the value
            curr.next = curr.next.next   # remove the node from the list
        else:
            curr = curr.next

    # Move to end of the updated list
    while curr.next:
        curr = curr.next

    # Append the collected nodes to the end
    while empty_list:
        node = empty_list.pop(0)
        node.next = None
        curr.next = node
        curr = curr.next

    return dummy.next

    
# Ask why do we need to curr.next again in the while loop

# Input: head = [1,4,3,2,5,2], x = 3
# Output: [1,2,2,4,3,5]
    
           