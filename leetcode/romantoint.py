
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
            try:
                if dict_roman[s[i]] >= dict_roman[s[i+1]]:
                    converted_number +=dict_roman[s[i]]
                    i+=1;cmp-=1
                else:
                    converted_number += (dict_roman[s[i+1]]- dict_roman[s[i]])
                    i+=2;cmp -=2
            except:
                converted_number += dict_roman[s[-1]]
                i+=1;cmp-=1
        # converted_number += dict_roman[s[-1]]
        return converted_number
    

