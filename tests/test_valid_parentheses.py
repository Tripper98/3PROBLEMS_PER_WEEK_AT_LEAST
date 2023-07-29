import unittest
from leetcode.valid_parentheses import Solution



class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_isValid(self):
        x = Solution().isValid(s="()[]{}")
        assert x == True, "Should be True"


if __name__ == '__main__':
    unittest.main()