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
            heapq.heappush(heap,(count[num],num)) #把当前数字以及它的 frequency 放入 min-heap

            # 如果 heap 超过 k 个元素，就删掉 frequency 最小的那个。
            if len(heap)>k:
                heapq.heappop(heap) # 因为是 min-heap，heappop() 自动删除最小 frequency。
        
        # 此时 heap 中只剩下 Top K frequent elements
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1]) # pop 出来的是:(frequency, number)
        return res



        
