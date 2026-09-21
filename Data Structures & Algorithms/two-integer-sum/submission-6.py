class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        incidies = {}
        for i,n in enumerate(nums):
            incidies[n] = i
        for i,n in enumerate(nums):
            diff = target - n
            if diff in incidies and incidies[diff]!=i:
                return [i,incidies[diff]]
        return []
  