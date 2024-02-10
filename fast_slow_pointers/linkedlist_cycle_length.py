"""
Given the head of a LinkedList with a cycle, find the length of the cycle.
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
            cycle_length = calculate_cycle_length(slow_pointer)
            return cycle_length 
    return False 

def calculate_cycle_length(slow_pointer):
    current = slow_pointer
    cycle_length = 0
    while True:
        current = current.next
        cycle_length += 1
        #break the loop once current iterates all the elements till slow pointer(finish a cycle)
        if current == slow_pointer:
            break 
    return cycle_length

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
The above algorithm runs in  O(N) time complexity and  O(1) space complexity.
"""
