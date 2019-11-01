# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root is None:
            return False
        q = list()
        q.append(root)
        while len(q) != 0:
            findx, findy = False, False
            size = len(q)
            for i in range(size):
                node = q.pop(0)
                if node.val == x:
                    findx = True
                if node.val == y:
                    findy = True

                # 避免属于同一个父节点
                if node.left is not None and node.right is not None:
                    if node.left.val == x and node.right.val == y:
                        return False
                    if node.left.val == y and node.right.val == x:
                        return False

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)

            if findx is True and findy is True:
                return True
            elif findx is False and findy is False:
                continue
            else:
                return False
        return False
