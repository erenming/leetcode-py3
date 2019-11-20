# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        return self.dfs(root, sum, 0)

    def dfs(self, root: TreeNode, sum: int, res: int) -> bool:
        if root is None:
            return False
        res += root.val
        if root.left is None and root.right is None and res == sum:
            return True
        return self.dfs(root.left, sum, res) or self.dfs(root.right, sum, res)
