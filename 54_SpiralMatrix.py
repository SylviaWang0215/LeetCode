class Solution(object):
    def spiralOrder(self, matrix):
        lis_direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        if matrix is []:
            return []
        width = len(matrix)
        length = len(matrix[0])
        size = width * length
        new_lis = []
        count = 0
        i, j = (0, -1)
        k = 0
        while count < size:
            temp_x, temp_y = lis_direction[k]
            if 0 > i + temp_x or i + temp_x >= width or 0 > j + temp_y or j + temp_y >= length\
                    or matrix[i + temp_x][j + temp_y] == "*":
                k = (k + 1) % 4
            temp_x, temp_y = lis_direction[k]
            i += temp_x
            j += temp_y
            new_lis.append(matrix[i][j])
            matrix[i][j] = "*"
            count += 1
        print new_lis
        return new_lis

lis1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lis2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
lis3 = []
f = Solution()
f.spiralOrder(lis3)
