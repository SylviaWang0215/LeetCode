class Solution(object):
    def generateMatrix(self, n):
        if n is 0:
            return []
        #create a list to store the all the element for matrix
        lis = range(1, n*n+1)

        #create direction
        lis_direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        k = 0
        i, j = (0, -1)
        count = 0
        dim = [0] * n
        A = [dim for _ in range(n)]

        while count < n*n:
            temp_x, temp_y = lis_direction[k]
            print i + temp_x, j + temp_y
            if 0 > i + temp_x or i + temp_x >= n or 0 > j + temp_y or j + temp_y >= n \
                    or A[i + temp_x][j + temp_y] != 0:
                k = (k + 1) % 4
            temp_x, temp_y = lis_direction[k]
            i += temp_x
            j += temp_y
            #print count, i, j, temp_x, temp_y
            A[i][j] = lis[count]
            count += 1

        return A

n1 = 3
n2 = 0
f = Solution()
print(f.generateMatrix(n1))
