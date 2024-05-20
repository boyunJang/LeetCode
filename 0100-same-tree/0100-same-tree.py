# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkTree(p, q):
            if p is None:
                if q is not None: return False
                else: return True
            if q is None: return False
            if p.val != q.val:
                return False
            if p.left is not None:
                if q.left is not None:
                    if not checkTree(p.left, q.left):
                        return False
                else:
                    return False
            elif q.left is not None:
                return False
            if p.right is not None:
                if q.right is not None:
                    if not checkTree(p.right, q.right):
                        return False
                else:
                    return False
            elif q.right is not None:
                return False
            return True

        return checkTree(p, q)