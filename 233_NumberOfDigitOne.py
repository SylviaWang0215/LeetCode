__author__ = 'mac'

class Solution(object):
    def countDigitOne(self, n):
        q = n
        x = 1
        while q > 0:
            digit = q % 10
            q /= 10

