# Definition for a Node.
from typing import List


class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        res = list()
        q = list()
        q.append(root)
        while len(q) != 0:
            size = len(q)
            level = list()
            for i in range(size):
                node = q.pop(0)
                level.append(node.val)
                for child in node.children:
                    q.append(child)
            res.append(level)
        return res
