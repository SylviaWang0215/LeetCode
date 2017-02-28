__author__ = 'mac'

class Solution(object):
    def letter(self, digits):
        dic = {"1": ["*"], "2": ["a", "b", "c"], "3": ["d", "e", "f"],
               "4": ["g", "h", "i"], "5": ["j", "k", "l"], "6": ["m", "n", "o"],
               "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"],
               "0": [" "]}
        temp = [""]
        lis = []
        length = len(digits)
        for i in range(length):
            key = digits[i]
            for item in dic.get(key):
                for x in temp:
                    new_str = x + item
                    lis.append(new_str)
            temp = lis
            lis = []
        return temp

