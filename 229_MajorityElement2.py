__author__ = 'mac'


class Solution(object):
    def majorityElement(self, nums):
        if not nums:
            return []
        length = len(nums)
        limit = round(length / 3)
        count = 0
        lis = []
        while count < 3 and len(nums) > limit:
            number = nums[0]
            value = nums.count(number)
            print number, value
            if value > limit:
                count += 1
                lis.append(number)
            nums = [x for x in nums if x != number]
        return lis
