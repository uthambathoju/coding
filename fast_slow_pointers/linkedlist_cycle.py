"""
Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.

Eg : HEAD -> 1-> 2 -> 3 -> 4 -> 5 -> 6 -> 3 -> 4 ->.....  (Linked List has a cycle)
     HEAD -> 2 -> 4 -> 6 -> 8 -> 10 (Linked List doesn't have  a cycle)

"""
"""
fast pointer moves by 2 steps
slow pointer moves by 1 step
the two pointers will definitely meet if the LinkedList has a cycle. A similar analysis can 
be done where the slow pointer moves first. Here is a visual representation of the above discussion:
"""
class Node:
    def __init__(self, value, next=None):
        self.value = value 
        self.next = next 
    
def has_cycle(head):
    #initialize fast and slow pointers with the first element(head)
    slow_pointer = head  
    fast_pointer = head 
    
    #check if fast_ptr is not none since it takes two steps in a single move and 
    #more likely chance to identify none values
    while fast_pointer is not None and fast_pointer.next is not None:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next 
        #if both of them match then LL has a cycle
        if slow_pointer == fast_pointer:
            return True 
    
    return False 

def main():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("LL has cycle : ", str(has_cycle(head)))
    head.next.next.next.next.next = head.next.next
    print("LL has cycle : ", str(has_cycle(head))) 
    head.next.next.next.next.next = head.next.next.next 
    print("LL has cycle : ", str(has_cycle(head))) 

main()
        
"""
Time Complexity #
As we have concluded above, once the slow pointer enters the cycle, the fast pointer will 
meet the slow pointer in the same loop. Therefore, the time complexity of our algorithm will be
O(N) where ‘N’ is the total number of nodes in the LinkedList.

Space Complexity #
The algorithm runs in constant space O(1).

"""
        
