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
        converted_number = dict_roman[s[0]]
        len_s = len(s)
        tmp = 0 ; i = 0
        while i != len_s-1:
        # for i in range(1, len_s-1):
            tmp = dict_roman[s[i]]
            if dict_roman[s[i+1]] <= tmp:
                converted_number += (tmp+dict_roman[s[i+1]])
            else:
                converted_number -= (dict_roman[s[i+1]]-tmp)
            i += 2

        return converted_number