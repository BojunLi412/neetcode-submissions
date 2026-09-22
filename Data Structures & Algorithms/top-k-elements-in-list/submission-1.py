class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            
            # 1. 统计每个数字出现次数
            # or in this way 
            # count[num] = count.get(num, 0) + 1
            if num not in count:
                count[num] = 1
            else:
                count[num] = count[num]+1
        sorted_count = sorted(
        count.items(),
        key=lambda x: x[1],
        reverse=True
    )

        # 取前 k 个数字
        result = []

        for num, freq in sorted_count[:k]:
            result.append(num)

        return result
            
    

        