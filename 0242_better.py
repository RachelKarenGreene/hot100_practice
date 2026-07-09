"""
LeetCode 242. 有效的字母异位词 — 优化版

原代码问题：
1. 统计 t 时，新字符赋值 1 后仍执行 += 1，首次出现会被记成 2
2. 比较写成 result_s[uu] != result_s[uu]，恒为 False，逻辑错误
3. return true 应为 return True
4. 维护两个字典 + 两次遍历，常数因子偏大

性能结论：
- 原思路时间复杂度 O(n)，空间 O(k)，方向正确
- 优化方向：单字典 / 固定长度数组 / Counter，减少一次遍历与一次哈希表
"""

from collections import Counter


class Solution:
    # 写法一：Counter（最简洁，面试首选）
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)

    # 写法二：长度 26 的数组（仅小写字母时最优常数）
    def isAnagram_array(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord("a")] += 1
        for ch in t:
            idx = ord(ch) - ord("a")
            counts[idx] -= 1
            if counts[idx] < 0:
                return False
        return True

    # 写法三：单字典加减（通用字符集，空间更省）
    def isAnagram_single_dict(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counts: dict[str, int] = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1
        for ch in t:
            if ch not in counts:
                return False
            counts[ch] -= 1
            if counts[ch] == 0:
                del counts[ch]
        return not counts


if __name__ == "__main__":
    sol = Solution()
    cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("ae", "eb", False),
        ("a", "ab", False),
    ]
    for s, t, expected in cases:
        assert sol.isAnagram(s, t) == expected
        assert sol.isAnagram_array(s, t) == expected
        assert sol.isAnagram_single_dict(s, t) == expected
    print("all tests passed")
