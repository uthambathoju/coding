"""
Given a binary tree, populate an array to represent its level-by-level traversal. 
You should populate the values of all nodes of each level from left to right in separate sub-arrays.

"""
#TC O(N)| SC O(N)
from collections import deque 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None 
    
def traverse(root):
    result = []
    if root is None:
        return result 
    queue = deque()
    queue.append(root)
    while queue:
        qlen = len(queue)
        level = []
        for _ in range(qlen):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right) 
        result.append(level)
    return result

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(10)
    root.right.right = TreeNode(5)
    print("tree level order traversal : ", str(traverse(root)))


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
O(N) as we need to return a list containing the level order traversal. We will also need 
�
(
�
)
O(N) space for the queue. Since we can have a maximum of 
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
