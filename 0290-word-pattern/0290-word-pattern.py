class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dic = {}
        s_dic = {}

        s_list = s.split(' ')

        if len(pattern) != len(s_list): return False

        for i in range(len(pattern)):
            tmp_p, tmp_s = pattern[i], s_list[i]
            if tmp_p not in pattern_dic and tmp_s not in s_dic:
                pattern_dic[tmp_p] = tmp_s
                s_dic[tmp_s] = tmp_p
            elif (tmp_p in pattern_dic and pattern_dic[tmp_p] != tmp_s) or (tmp_s in s_dic and s_dic[tmp_s] != tmp_p):
                return False

        return True