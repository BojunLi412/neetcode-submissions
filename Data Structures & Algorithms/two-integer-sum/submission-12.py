class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # value -> index

        # Traverse the array once
        for i, n in enumerate(nums):
            # The other number we need
            diff = target - n

            # If diff appeared before, we found the answer
            if diff in prevMap:
                return [prevMap[diff], i]

            # Otherwise, store the current number and its index
            # for future elements to use
            prevMap[n] = i

        # No valid pair found
        return []


        