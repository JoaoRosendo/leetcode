class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        
        while i < j:
            sum_result = numbers[i] + numbers[j]
            
            if sum_result > target:
                j -= 1
            elif sum_result < target:
                i += 1
            else:
                return [i + 1, j + 1]
        
        return False