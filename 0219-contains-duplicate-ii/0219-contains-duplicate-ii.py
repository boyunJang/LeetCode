class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if k == 0 or len(nums) < 2: return False
        for i in range(len(nums)):
            for j in range(1, k + 1):
                if i + j >= len(nums): break
                if nums[i] == nums[i + j]: return True
        return False
        