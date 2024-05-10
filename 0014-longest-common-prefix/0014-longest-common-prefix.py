class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = strs[0]
        for idx, input in enumerate(strs):
            if idx == 0: continue
            i = 0
            for c in output:
                if i >= len(input): break
                if c != input[i]:break
                i += 1
            if i == 0:
                output = ""
                break
            output = output[:i]

        return output