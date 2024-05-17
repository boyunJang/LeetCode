class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0: return []
        start = nums[0]
        end = nums[0]
        result = []
        for i in range(1, len(nums)):
#             print(nums[i], start, end)
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))
                start = nums[i]
                end = nums[i]
            
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end))
            
        return result

        