# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        self.dfs(root, "", res)
        return res

    def dfs(self, root: TreeNode, ls, res):
        if not root.left and not root.right:
            res.append(ls + str(root.val))
        if root.left:
            self.dfs(root.left, ls+str(root.val)+"->", res)
        if root.right:
            self.dfs(root.right, ls+str(root.val)+"->", res)
