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
        # Python 的 heapq 是 min-heap
        #
        # heap 里面存:
        # (frequency, number)
        #
        # 例如:
        # (3, 1) 表示数字 1 出现了 3 次
        #
        # 我们让 heap 始终最多只有 k 个元素，
        # 这样最后留下来的就是 frequency 最大的 k 个数字。    
        heap = []
        for num in count.keys():
            heapq.heappush(heap,(count[num],num))
            if len(heap)>k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



        
