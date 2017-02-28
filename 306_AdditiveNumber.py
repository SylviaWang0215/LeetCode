__author__ = 'mac'


class Solution(object):
    def isAdditiveNumber(self, num):
        length = len(num)
        if length < 3:
            return False
        for i in range(1, length-2):
            for j in range(i+1, length-1):
                a = num[:i]
                b = num[i: j]
                if b != str(int(b)):
                    continue
                while j < length:
                    c = str(int(a) + int(b))
                    if not num.startswith(c, j):
                        break
                    j += len(c)
                    a, b = b, c
                if j == length:
                    return True
        return False

