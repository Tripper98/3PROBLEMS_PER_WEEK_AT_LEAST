import unittest
from leetcode.romantoint import Solution

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_fproblem(self):
        x = Solution().romanToInt(s= "MCMXCIV")
        print(x)
        assert x == 1994, "Should be 58"


if __name__ == '__main__':
    unittest.main()