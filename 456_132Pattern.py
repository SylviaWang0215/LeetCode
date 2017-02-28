__author__ = 'mac'


class Solution(object):
    def find132pattern(self, nums):
        length = len(nums)
        if length < 3:
            return False
        lis = nums
        while nums:
            value = nums[0]
            index = lis.index(value)
            temp = [x for x in lis[index:] if x > value]
            #print index, temp
            if temp:
                sorted_temp = sorted(temp)
                if temp != sorted_temp:
                    return True
            nums = [x for x in nums if x < value and x < sorted_temp[0]]
        return False
