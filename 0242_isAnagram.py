class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        result_s = {}
        result_t = {}
        for ss in s:
            if ss not in result_s:
                result_s[ss] = 1
            else:
                result_s[ss] += 1
        for tt in t:
            if tt not in result_t:
                result_t[tt] = 1
            else:
                result_t[tt] += 1

        unique = set(s)

        for uu in unique:
            if uu not in result_t or result_s[uu] != result_t[uu]:
                return False
        return True

class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        record = [0]*26
        for ss in s:
            record[ord(ss) - ord('a')] += 1
        for tt in t:
            record[ord(tt) - ord('a')] -= 1
        for i in range(26):
            if record[i] != 0:
                return False
        return True