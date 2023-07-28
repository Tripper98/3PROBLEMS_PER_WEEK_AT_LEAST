class Solution(object):

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        j = 0 ; min_str = 0
        len_strs = len(strs)
        list_aux = strs

        while j < len_strs-1:
            res = ""
            list_to_check = list_aux[0:2]
            len_a = len(list_to_check[0])
            len_b = len(list_to_check[1])

            if len_a > len_b:
                min_str = len_b
            else:
                min_str = len_a

            for i in range(min_str):
                if list_to_check[0][i] == list_to_check[1][i]:
                    res += list_to_check[1][i]
                else:
                    break
                    
            list_aux = list_aux[2:]
            list_aux.insert(0, res)
            j += 1

        return res
    

import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_fproblem(self):
        x = Solution().longestCommonPrefix(strs=["cir","car"])
        print(x)
        assert x == "c", "Should be \"fl\""


if __name__ == '__main__':
    unittest.main()