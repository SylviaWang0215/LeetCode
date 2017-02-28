__author__ = 'mac'


class Solution(object):
    def HammingDistance(self, x, y):
        s1 = "{0:b}".format(x)
        s2 = "{0:b}".format(y)
        count = 0
        len1 = len(s1)
        len2 = len(s2)
        if len1 < len2:
            s1 = s1.rjust(len2)
            s1 = s1.replace(" ", "0")
        else:
            s2 = s2.rjust(len1)
            s2 = s2.replace(" ", "0")
        length = len(s1)
        for i in range(length):

            if s1[i] != s2[i]:
                count += 1

        #print(s1)
        #print(s2)
        return count

x = 1
y = 4
f = Solution()
print(f.HammingDistance(x, y))


