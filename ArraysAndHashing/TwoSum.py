class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values_and_index = {}
        for i, n in enumerate(nums):
            values_and_index[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in values_and_index and values_and_index[diff] != i:
                return [i, values_and_index[diff]]
