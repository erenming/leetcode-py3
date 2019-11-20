# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        return self.dfs(root1) == self.dfs(root2)

    def dfs(self, root: TreeNode):
        res = []
        if not root:
            return res

        stack = list()  # stack
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            if not node.left and not node.right:
                res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res
