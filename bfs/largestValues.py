# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        res = list()

        q = deque()
        q.append(root)
        while len(q) != 0:
            size = len(q)
            level = list()
            for _ in range(size):
                node = q.popleft()
                level.append(node.val)
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            res.append(max(level))
        return res
