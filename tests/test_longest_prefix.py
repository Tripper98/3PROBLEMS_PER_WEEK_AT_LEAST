import unittest
from leetcode.longest_prefix import Solution



class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_fproblem(self):
        x = Solution().longestCommonPrefix(strs=["cir","car"])
        print(x)
        assert x == "c", "Should be \"fl\""


if __name__ == '__main__':
    unittest.main()