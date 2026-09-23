class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        # 1. 统计每个数字出现次数
        for num in nums:
            count[num] = 1 + count.get(num, 0)

        # 2. freq[i] = 出现 i 次的数字列表
        freq = [[] for _ in range(len(nums) + 1)]

        for num, cnt in count.items():
            freq[cnt].append(num)

        # 3. 从高频率往低频率找
        res = []

        for cnt in range(len(freq) - 1, 0, -1):
            for num in freq[cnt]:
                res.append(num)

                if len(res) == k:
                    return res


                    