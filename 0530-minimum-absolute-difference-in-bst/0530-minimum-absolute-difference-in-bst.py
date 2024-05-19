# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def get_min(node):
            if node.left is not None:
                return get_min(node.left)
            else:
                return node.val
        def get_max(node):
            if node.right is not None:
                return get_max(node.right)
            else:
                return node.val
        def get_diff(node, min_diff):
            if node.left is not None:
                min_diff = min(min(min_diff, node.val - get_max(node.left)), get_diff(node.left, min_diff))
            if node.right is not None:
                min_diff = min(min(min_diff, get_min(node.right) - node.val), get_diff(node.right, min_diff))
            return min_diff

        return get_diff(root, 10**5 + 1)