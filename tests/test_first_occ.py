
import unittest
from leetcode.first_occ import Solution

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_first_occ(self):
        for i, j, k in (  
            ("mississippi", "sipp", 6),
            ("bbbbababbbaabbba", "abb", 6),
            ("hello", "ll", 2),
        ):
            
            x = Solution().strStr(haystack=i, needle=j)
            assert x == k, f"Should be {k}"


if __name__ == '__main__':
    unittest.main()