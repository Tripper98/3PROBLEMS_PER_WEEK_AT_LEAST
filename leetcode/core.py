import unittest

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict_roman = {
            'I':1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        converted_number = 0
        i = 0 ; cmp = len(s)

        while cmp >=1:
            if dict_roman[s[i]] >= dict_roman[s[i+1]]:
                converted_number +=dict_roman[s[i]]
                i+=1;cmp-=1
            else:
                converted_number += (dict_roman[s[i+1]]- dict_roman[s[i]])
                i+=2;cmp -=2
            print(converted_number)
        # converted_number += dict_roman[s[-1]]
        return converted_number
    

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_fproblem(self):
        x = Solution().romanToInt(s= "LVIII")
        print(x)
        assert x == 58, "Should be 58"


if __name__ == '__main__':
    unittest.main()
