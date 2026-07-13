# 导入类型注解依赖
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            # 打印排序后的字符列表，观察标准化key
            char_list = sorted(s)
            print(f"原字符串：{s}，排序后字符列表：{char_list}")
            # 生成统一哈希分组key
            sorted_key = "".join(char_list)
            # 字典不存在该key则初始化空列表
            if sorted_key not in hash_map:
                hash_map[sorted_key] = []
            # 将原字符串加入对应分组
            hash_map[sorted_key].append(s)
        # 提取所有分组列表作为返回结果
        return list(hash_map.values())

# 测试运行入口
if __name__ == "__main__":
    sol = Solution()
    test_input = ["eat","tea","tan","ate","nat","bat"]
    res = sol.groupAnagrams(test_input)
    print("\n最终分组结果：", res)