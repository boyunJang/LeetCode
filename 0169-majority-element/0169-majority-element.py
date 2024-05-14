from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dic = Counter(nums)
        for key, val in sorted(num_dic.items(), key = lambda x: x[1], reverse = True):
            return key

        