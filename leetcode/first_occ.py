class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
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
    