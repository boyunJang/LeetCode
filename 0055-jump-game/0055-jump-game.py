class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1: return True
        visitable = [0] * len(nums)
        visitable[0] = 1
        for idx, num in enumerate(nums):
#             print(idx, num, visitable[idx])
            if visitable[idx]:
                for i in range(1, num + 1):
#                     print(idx + i)
                    if idx + i == len(nums) - 1: return True
                    visitable[idx + i] = 1
        return False



        