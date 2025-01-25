import unittest
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_words = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            sorted_words[sorted_word].append(word)
        return [anagrams for anagrams in sorted_words.values()]
                    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_group_anagrams_basic(self):
        strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        expected = [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        result = self.solution.groupAnagrams(strs)
        result_sorted = [sorted(group) for group in result]  # Sort each group to match the expected
        self.assertCountEqual(result_sorted, [sorted(group) for group in expected])

    def test_group_anagrams_empty(self):
        strs = []
        expected = []
        result = self.solution.groupAnagrams(strs)
        self.assertEqual(result, expected)

    def test_group_anagrams_no_anagrams(self):
        strs = ["abc", "def", "ghi"]
        expected = [["abc"], ["def"], ["ghi"]]
        result = self.solution.groupAnagrams(strs)
        result_sorted = [sorted(group) for group in result]
        self.assertCountEqual(result_sorted, [sorted(group) for group in expected])

    def test_group_anagrams_all_same(self):
        strs = ["abc", "abc", "abc"]
        expected = [["abc", "abc", "abc"]]
        result = self.solution.groupAnagrams(strs)
        result_sorted = [sorted(group) for group in result]
        self.assertCountEqual(result_sorted, [sorted(group) for group in expected])

    def test_group_anagrams_multiple_groups(self):
        strs = ["listen", "silent", "enlist", "abc", "cab", "bca"]
        expected = [["listen", "silent", "enlist"], ["abc", "cab", "bca"]]
        result = self.solution.groupAnagrams(strs)
        result_sorted = [sorted(group) for group in result]
        self.assertCountEqual(result_sorted, [sorted(group) for group in expected])

if __name__ == "__main__":
    unittest.main()
