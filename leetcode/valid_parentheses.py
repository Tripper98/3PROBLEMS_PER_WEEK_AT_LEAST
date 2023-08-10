class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict_par = {
            "(" : ")",
            "{" : "}",
            "[" : "]",
        }
        aux_s = s
        len_s = len(aux_s)
        i = len_s
        # cmp = 0

        if len_s%2 != 0:
            return False

        while i != 0: # TO FIX
            cmp = 0 
            # print(f"i >> {i}")
            for j in range(len(aux_s)-1):
                # print(j)
                if aux_s[j] in dict_par.keys():
                    if dict_par[aux_s[j]] == aux_s[j+1]:
                        # String to list 
                        # print(f"Before >> {aux_s}")
                        list_s = list(aux_s)
                        list_s[j] = ''
                        list_s[j+1] = ''
                        aux_s = ''.join(list_s)
                        # print(f"After >> {aux_s}")
                        cmp = 1
                        i -= 2
                        break
            if cmp == 0:
                return False
            
        return True