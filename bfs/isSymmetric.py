from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        q = deque()
        q.append(root)
        while len(q) != 0:
            size = len(q)
            level = list()
            for _ in range(size):
                node = q.popleft()
                if node is not None:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                else:
                    level.append(None)
            length = len(level)
            mid = length // 2
            if length > 1 and level[0:mid] != list(reversed(level[mid:])):
                return False
        return True


if __name__ == '__main__':
    def deserialize(string):
        if string == '{}':
            return None
        nodes = [None if val == 'null' else TreeNode(int(val))
                 for val in string.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    t = deserialize('[1,2,2,null,3,null,3]')
    print(Solution().isSymmetric(t))
