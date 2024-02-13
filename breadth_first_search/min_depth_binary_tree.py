"""
Find the minimum depth of a binary tree. 
The minimum depth is the number of nodes along the shortest path from the root node to 
the nearest leaf node.
"""

from collections import deque 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None 
        self.right = None 

# TC O(N) | SC O(N)
def min_depth_in_tree(root):
    if root is None:
        return 0 
    minimum_depth = 0
    result = []
    queue = deque()
    queue.append(root)
    while queue:
        minimum_depth += 1
        qlen = len(queue) 
        for _ in range(qlen):
            currentNode = queue.popleft()
            #check if it is a leaf node
            if not currentNode.left and not currentNode.right:
                return minimum_depth

            if currentNode.left:
                queue.append(currentNode.left)
            
            if currentNode.right:
                queue.append(currentNode.right)


def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("min depth tree :: ", min_depth_in_tree(root))
    root.left.left= TreeNode(9)
    root.right.left.left= TreeNode(11)
    print("min depth tree :: ", min_depth_in_tree(root))

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
