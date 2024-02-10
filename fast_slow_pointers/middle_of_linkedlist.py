"""
Given the head of a Singly LinkedList, write a method to return the middle node of the LinkedList.
If the total number of nodes in the LinkedList is even, return the second middle node.
"""

"""
We can use the Fast & Slow pointers method such that the fast pointer is always twice 
the nodes ahead of the slow pointer. This way, when the fast pointer reaches the end of the LinkedList, 
the slow pointer will be pointing at the middle node.

"""
class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 


def middle_of_linkedlist(head):
    fast_ptr = head
    slow_ptr = head 
    while fast_ptr is not None and  fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    
    return slow_ptr

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LL has cycle : ", str(middle_of_linkedlist(head)))
    head.next.next.next.next.next = head.next.next
    print("LL has cycle : ", str(middle_of_linkedlist(head))) 
    head.next.next.next.next.next = head.next.next.next 
    print("LL has cycle : ", str(middle_of_linkedlist(head))) 

main()


"""
Time complexity #
The above algorithm will have a time complexity of 
O(N) where ‘N’ is the number of nodes in the LinkedList.

Space complexity #
The algorithm runs in constant space O(1).

"""
