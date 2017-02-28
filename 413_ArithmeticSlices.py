__author__ = 'mac'

class Solution(object):
    def findArithmetic(self, A, start, end, diff):
        length = len(A)
        if end == length - 1:
            return Solution.ret.append(A[start:end + 1])
        if A[end + 1] - A[end] == diff:
            self.findArithmetic(A, start, end+1, diff)
        return Solution.ret.append(A[start: end+1])

    def numberOfArithemticSlices(self, A):
        length = len(A)
        Solution.ret = []
        if not A:
            return 0
        if length == 1:
            return 0
        for i in range(length-2):
            if A[i + 2] - A[i + 1] == A[i + 1] - A[i]:
                diff = A[i + 2] - A[i + 1]
                self.findArithmetic(A, i, i+2, diff)
        if not Solution.ret:
            return 0
        num = len(Solution.ret)
        print Solution.ret
        return num

s1 = [1, 2, 3, 4, 5]
f = Solution()
print f.numberOfArithemticSlices(s1)