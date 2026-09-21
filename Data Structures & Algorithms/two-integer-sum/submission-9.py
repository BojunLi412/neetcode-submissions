class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Dictionary: number -> its index in nums
        indices = {}

        # First pass:
        # store every number and its index in the dictionary
        for i, n in enumerate(nums):
            indices[n] = i

        # Second pass:
        # for each number n, find the number needed to reach target
        for i, n in enumerate(nums):
            diff = target - n

            # Check whether the needed number exists
            # and make sure we are not using the same element twice
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

        # No valid pair found
        return []
        incidies = {}
        for i,n in enumerate(nums):
            incidies[n] = i
        for i,n in enumerate(nums):
            diff = target - n
            if diff in incidies and incidies[diff]!=i:
                return [i,incidies[diff]]
        return []
  