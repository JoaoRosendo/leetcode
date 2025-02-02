class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_and_freq = defaultdict(int)
        freq = [[] for i in range( len(nums) + 1)]

        for num in nums:
            nums_and_freq[num] += 1
        
        for num, frequency in nums_and_freq.items():
            freq[frequency].append(num)
        
        solution = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                solution.append(num)
                if len(solution) == k:
                    return solution

class SlowerSolution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_and_freq = defaultdict(int)
        for num in nums:
            nums_and_freq[num] += 1
        
        list_w_items = []
        for num, frequency in nums_and_freq.items():
            list_w_items.append([frequency, num])
        list_w_items.sort()

        solution = []

        while len(solution) < k:
            solution.append(list_w_items.pop()[1])
        return solution
