class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0
        for num in nums_set:
            if num - 1 not in nums_set:
                help = num
                cur = 0
                while help in nums_set:
                    help += 1
                    cur += 1
                if longest < cur:
                    longest = cur
        return longest

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 转为集合，实现O(1)查询
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # 只有当前数字是一段连续序列的起点时，才进入统计
            if num - 1 not in num_set:
                current_num = num
                current_length = 0
                # 向后遍历所有连续数字
                while current_num in num_set:
                    current_num += 1
                    current_length += 1
                # 更新全局最长长度
                max_length = max(max_length, current_length)
        return max_length

# 本地测试入口
if __name__ == "__main__":
    solution = Solution()
    print(solution.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 输出 4
    print(solution.longestConsecutive([]))                      # 输出 0
    print(solution.longestConsecutive([0, -1]))                 # 输出 2
    print(solution.longestConsecutive([1, 2, 0, 1]))            # 输出 3