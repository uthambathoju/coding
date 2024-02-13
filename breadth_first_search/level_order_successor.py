"""
Given a binary tree and a node, find the level order successor of the given node in the tree. 
The level order successor is the node that appears right after the given node in the level order traversal.
"""
#In input , we will be given a node and we need to return the next element of the given node
from collections import deque 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None 

#if there is no level differentation required, while level should be okay else while with for loop
# is required , eg: tree level traversal , min depth of tree , max depth of tree
def level_order_successor(root, givenNode):
    if root is None:
        return 
    queue = deque()
    queue.append(root)
    while queue:
        currentNode = queue.popleft()
        if currentNode.left:
            queue.append(currentNode.left)
        if currentNode.right:
            queue.append(currentNode.right)
        
        if currentNode.val == givenNode:
            break 
    return queue[0] if queue else None 
    

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(10)
    root.right.right = TreeNode(5)
    res = level_order_successor(root, 12)
    if res:
        print(res.val)
    else:
        print("failed")
    res1 = level_order_successor(root, 9)
    print(res1.val)

main()
"""
Time complexity #
The time complexity of the above algorithm is 
�
(
�
)
O(N), where ‘N’ is the total number of nodes in the tree. This is due to the fact that we traverse each node once.

Space complexity #
The space complexity of the above algorithm will be 
�
(
�
)
O(N) which is required for the queue. Since we can have a maximum of 
�
/
2
N/2 nodes at any level (this could happen only at the lowest level), therefore we will need 
�
(
�
)
O(N) space to store them in the queue.
"""
