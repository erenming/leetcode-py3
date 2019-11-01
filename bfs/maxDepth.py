import queue


# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


    class Solution:
        def maxDepth(self, root: 'Node') -> int:
            if root is None:
                return 0
            depth = 0
            q = list()
            q.append(root)
            while len(q) != 0:
                size = len(q)
                for i in range(size):
                    node = q.pop(0)
                    for child in node.children:
                        q.append(child)
                depth += 1

            return depth
