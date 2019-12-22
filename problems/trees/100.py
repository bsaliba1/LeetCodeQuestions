# 100. Same Tree
# Link: https://leetcode.com/problems/same-tree/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    @staticmethod
    def isSameTree(x: TreeNode, y: TreeNode) -> bool:
        if x is not None and y is None:
            return False
        if y is not None and x is None:
            return False
        if x is None and y is None:
            return True
        if x.val != y.val:
            return False

        if Solution().isSameTree(x.left, y.left) and Solution().isSameTree(x.right, y.right):
            return True
        else:
            return False

        return True
