# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    moves = 0

    def distributeCoins(self, root: TreeNode) -> int:
        self.nums_and_coins(root)
        return self.moves

    # return (# of nodes, # of coins)
    def nums_and_coins(self, root: TreeNode):
        if root is None:
            return 0, 0
        left = self.nums_and_coins(root.left)
        right = self.nums_and_coins(root.right)
        self.moves += abs(left[0] - left[1]) + abs(right[0] - right[1])
        return left[0] + right[0] + 1, left[1] + right[1] + root.val
