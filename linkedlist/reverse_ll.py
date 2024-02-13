"""
Given the head of a Singly LinkedList, reverse the LinkedList. 
Write a function to return the new head of the reversed LinkedList.
"""
class Node:
    def __init__(self, value, next=None):
        self.value=value
        self.next= next
    
    def print_ll(self):
        tmp = self 
        while tmp is not None:
            print(tmp.value , end=" ")
            tmp = tmp.next 

def reverse_linkedlist(head):
    previous, current, next = None, head, None 
    while current is not None:
        next = current.next
        current.next = previous 
        previous = current # after the reverse is completed, this line is to for the upcoming elements to point to prev element
        current = next  # this line is also to move forward to take upcoming element as current ele
    return previous


def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.print_ll()
    res=reverse_linkedlist(head)
    res.print_ll()


main()
