from collections import Counter

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        num_dic = Counter(nums)
        for key, val in num_dic.items():
            while val > 2:
                nums.remove(key)
                val -= 1

        return len(nums)