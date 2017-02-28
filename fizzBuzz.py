__author__ = 'mac'


class Solution(object):
    def fizzBuzz(self, n):
        lis = []
        for i in range(1, n+1):
            if i % 3 == 0:
                if i % 5 == 0:
                    lis.append("FizzBuzz")
                else:
                    lis.append("Fizz")
            else:
                if i % 5 == 0:
                    lis.append("Buzz")
                else:
                    lis.append(str(i))
        return lis

n = 15
f = Solution()
print(f.fizzBuzz(n))