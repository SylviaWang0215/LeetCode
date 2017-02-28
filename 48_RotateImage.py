__author__ = 'mac'


class Solution(object):
    def rotate(self, matrix):
        length = len(matrix)
        new_matrix = []
        for i in range(length):
            new_lis = []
            for j in range(length-1, -1, -1):
                value = matrix[j][i]
                new_lis = new_lis + [value]
            new_matrix.append(new_lis)
        print new_matrix
        matrix = new_matrix
        print(matrix)


lis1 = [[1, 2], [3, 4]]
f = Solution()
f.rotate(lis1)
#print(lis1)