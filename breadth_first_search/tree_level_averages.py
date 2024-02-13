""" Given a binary tree, populate an array to represent the averages of all of its levels. """


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
        level_sum = 0 
        for _ in range(qlen):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right) 
        result.append(level_sum / qlen)
    return result

def main():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    print("tree level order traversal : ", str(traverse(root)))


main()
