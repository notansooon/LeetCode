class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
  
  
node1 = Node(1,Node(2, Node(3, Node(2))))



def freq(head, val):
    count = 0
    curr = head
    while curr:
        if curr.value == val:
            count+=1
        curr = curr.next
    return count
num = freq(node1, 2)
print(num)
 
 
