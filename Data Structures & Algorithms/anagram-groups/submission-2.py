class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict(list):
        # 如果某个 key 不存在，会自动创建一个空 list []
        groups = defaultdict(list)

        for s in strs:
            # 创建长度为 26 的数组
            # 分别记录 a-z 每个字母出现的次数
            #
            # index:
            # 0 -> a
            # 1 -> b
            # 2 -> c
            # ...
            # 25 -> z
            count = [0] * 26

            for char in s:
                # ord(char) - ord('a') 把字母转换成 0~25 的位置
                #
                # 例如:
                # 'a' -> 97 - 97 = 0
                # 'b' -> 98 - 97 = 1
                # 'c' -> 99 - 97 = 2
                #
                # 当前字母出现一次，对应位置 +1
                count[ord(char) - ord('a')] += 1

            # 最重要的一步：
            #
            # count 是 list，例如:
            # [1, 0, 0, 0, 1, ..., 1, ...]
            #
            # 它表示这个字符串每个字母出现了多少次。
            # 所有 anagram 的 count 都会完全一样。
            #
            # 但是！！！Python 的 dictionary key 必须是 hashable（不可变的）。
            #
            # list 是可变的 mutable：
            # count[0] = 10
            # 所以 list 不能作为 dictionary 的 key。
            #
            # tuple 是不可变的 immutable，所以可以被 hash，
            # 因此 tuple 可以作为 dictionary 的 key。
            #
            # 所以必须把:
            # list  -> tuple
            #
            # 错误：
            # groups[count].append(s)
            #
            # 正确：
            # groups[tuple(count)].append(s)
            groups[tuple(count)].append(s)

        # 返回所有分好的组
        return list(groups.values())

        