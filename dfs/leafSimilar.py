# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        l1 = list()
        l2 = list()
        self.dfs(root1, l1)
        self.dfs(root2, l2)
        return l1 == l2

    def dfs(self, node: TreeNode, leaves):
        if node is None:
            return leaves
        if node.left is None and node.right is None:
            leaves.append(node.val)
        if node.left is not None:
            self.dfs(node.left, leaves)
        if node.right is not None:
            self.dfs(node.right, leaves)