class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # len_needle = len(needle)
        # cmp = 0 ; j = 0 ;  i = 0 

        # if needle in haystack:
        #     while i < len_needle:
        #         print(haystack[0:i])
        #         if needle[i] == haystack[i]:
        #             i += 1 ; cmp += 1 # ; j = i ; 
        #         else:
        #             i = 0 ; cmp = 0
        #             haystack_list = list(haystack)
        #             del haystack_list[i]
        #             haystack = "".join(haystack_list)
        #             print(haystack)
        #         j += 1
        #         print(cmp)
        #         print(f"j >>> {j}")
                
        #         print(j - len_needle)
        #         if cmp == len_needle:
        #             return j - len_needle
        #     return j - len_needle
            
        # return -1  
        if needle not in haystack:
            return -1 
        
        len_haystack = len(haystack)
        len_needle = len(needle)
        indice = 0 ; cmp = 0 ; i = 0

        # for i in range(len_haystack):
        while indice < len_haystack :
            i = indice
            for j in range(len_needle):
                if haystack[i] == needle[j]:
                    # print(haystack[i], needle[j])
                    i += 1
                    cmp += 1
                else:
                    # i += 1
                    break
                
            #     print(cmp)
            # print("###")
            if cmp == len_needle:
                return indice
            else : 
                indice += 1
                cmp = 0 
        return indice
    


import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_first_occ(self):
        # x = Solution().isValid(s="()")
        # assert x == True, "Should be True"


        for i, j, k in (  
            ("mississippi", "sipp", 6),
            ("bbbbababbbaabbba", "abb", 6),
            ("hello", "ll", 2),
        ):
            
            x = Solution().strStr(haystack=i, needle=j)
            print(x)
            assert x == k, f"Should be {k}"


if __name__ == '__main__':
    unittest.main()