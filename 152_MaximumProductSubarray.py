import numpy as np


class Solution(object):
    def maxProduct(self, nums):

        length = len(nums)

        if length == 1:
            return nums[0]

        max_num = 0

        for i in range(length):
            temp_lis = nums[i:]
            if nums[i] == 0:
                temp = 0
                if temp >= max_num:
                    max_num = temp
                continue
            if 0 in temp_lis and temp_lis.index(0) != 0:
                index_zero = temp_lis.index(0)
                temp_lis = temp_lis[:index_zero]

            neg_lis = [x for x in temp_lis if x < 0]

            if len(neg_lis) % 2 == 1:
                index_last_neg = temp_lis.index(neg_lis[len(neg_lis) - 1])
                temp_lis = temp_lis[:index_last_neg]
            temp = np.prod(temp_lis)
            if temp_lis == []:
                temp = nums[i]
            if temp > max_num:
                max_num = temp
            if temp_lis == nums[i:]:
                return int(max_num)
        return int(max_num)

lis1 = [1, -2, -3, 4]
lis2 = [-3, -4]
lis3 = [-1, 0, -2]
f = Solution()


print f.maxProduct(lis1)
