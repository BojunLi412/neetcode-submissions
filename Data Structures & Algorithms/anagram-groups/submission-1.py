class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}  # key: 排序后的字符串, value: 所有属于这一组的原字符串

        for s in strs:
            # anagram 排序后一定相同
            # 例如:
            # "eat" -> "aet"
            # "tea" -> "aet"
            # "ate" -> "aet"
            # 所以可以把排序后的结果作为分组的 key
            key = ''.join(sorted(s))

            # 如果这个 key 第一次出现，就先创建一个空 list
            if key not in groups:
                groups[key] = []

            # 把当前字符串加入对应的 anagram 组
            groups[key].append(s)

        # groups 最后类似:
        # {
        #     "aet": ["eat", "tea", "ate"],
        #     "ant": ["tan", "nat"],
        #     "abt": ["bat"]
        # }
        #
        # 题目只需要每一组字符串，不需要 key
        return list(groups.values())
       