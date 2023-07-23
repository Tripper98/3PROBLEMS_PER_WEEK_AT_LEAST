
import unittest
import sys

sys.path.append("E:\Entertainment\Coding\3PROBLEMS_PER_WEEK_AT_LEAST\leetcode")
import leetcode


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_factorial_n(self):
        x = print(leetcode.core.Solution().romanToInt(s= "LVIII")) 
        assert x == 58, "Should be 58"


if __name__ == '__main__':
    unittest.main()
