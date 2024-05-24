from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        deq = deque([(root, 0)])
        average = {}
        while len(deq) > 0:
            node, level = deq.popleft()
            if level not in average:
                average[level] = [0, 0]
            average[level][0] += node.val
            average[level][1] += 1
            if node.left is not None:
                deq.append((node.left, level + 1))
            if node.right is not None:
                deq.append((node.right, level + 1))

        result = []

        for key, val in sorted(average.items(), key = lambda x: x[0], reverse = False):
            result.append(round(float(val[0]) / float(val[1]), 5))

        return result