class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sorted_num = sorted(nums)
        for i in range(0,len(sorted_num)-1):
            if sorted_num[i] == sorted_num[i+1]:
                return True

        return False
            
        