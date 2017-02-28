__author__ = 'mac'


class Solution(object):
    def countBits(self, num):
        lis = [0]
        if num == 0:
            return lis
        for i in range(1, num+1):
            value = lis[i&(i-1)] + 1
            #i & i-1 返回公有的某一位binary表示下的数字
            print i, i-1, i&i-1
            lis = lis + [value]
        return lis

n1 = 10
f = Solution()
print(f.countBits(n1))
