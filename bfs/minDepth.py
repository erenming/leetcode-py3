# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

from collections import deque

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        depth = 0
        q = deque()
        q.append(root)
        while len(q) != 0:
            depth += 1
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left is None and node.right is None:
                    return depth
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return depth
