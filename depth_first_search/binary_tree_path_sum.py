"""
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf 
such that the sum of all the node values of that path equals ‘S’.
"""

from collections import deque 
class TreeNode:
    def __init__(self, val, left=None,right=None):
        self.val = val
        self.left, self.right = left, right


#in recursive call , the call stack will build from root to leaf node by checking left nodes and if the desired
#value is false then the respective return will happen back-wards till root by checking the left.right 
#nodes and once the root is arrived  then it will start moving to right side nodes
def has_path(root, givenSum):
    if root is None:
        return False 
    # if current node is leaf and its value equal to the sum , we found the path
    if root.val == givenSum  and root.left is None and root.right is None:
        return True
    
    # recursive call to traverse the left sub tree and right sub tree
    # return true if any of the two recursive calls return true
    print(root.val, ":: ", givenSum, "::", givenSum - root.val)
    
    return has_path(root.left, givenSum - root.val) or has_path(root.right, givenSum - root.val)

def has_path_method_2(root, givenSum):
    def dfs(node, curSum):
        if not node:
            return False 
        
        curSum += node.val 
        if not node.left and not node.right:
            return curSum == givenSum 
    
        return dfs(node.left, curSum) or dfs(node.right, curSum)

    return dfs(root, 0)

def main():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    #print("tree has path : ", str(has_path(root, 23)))
    print("tree has path : ", str(has_path(root, 18)))


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
O(N) in the worst case. This space will be used to store the recursion stack. The worst case will happen when the given tree is a linked list (i.e., every node has only one child).
"""
