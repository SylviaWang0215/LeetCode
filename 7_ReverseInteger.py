__author__ = 'mac'


class Solution(object):
    def reverse(self, x):
        s = str(x)
        sign = ""
        if s[0] == "-" or s[0] == "+":
            sign = s[0]
            s = s[1:]
        s = s[::-1]
        length = len(s)
        sub = s
        for i in range(length):
            if s[i] == '0' and length == 1:
                return 0
            if s[i] == '0':
                sub = sub[1:]
            else:
                break
        if sign != "":
            sub = sign + sub
        sub = int(sub)
        if abs(sub) > 2147483647:
            return 0
        return sub

x1 = -250
f = Solution()
print(f.reverse(x1))