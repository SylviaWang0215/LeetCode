__author__ = 'mac'


class Solution(object):
    def minMoves2(self, nums):
        average = (sum(nums) + 0.0)/len(nums)

        if average in nums:
            lower = [average - x for x in nums if x < average]
            larger = [x - average for x in nums if x > average]
            return sum(lower) + sum(larger)
        else:
            lower = [x for x in nums if x < average]
            larger = [x for x in nums if x > average]
            if len(lower) > len(larger):
                average = round(average)
            else:
                average = round(average + 0.5)
            new_lower = [average - x for x in nums if x < average]
            new_larger = [x - average for x in nums if x > average]
            return sum(new_larger) + sum(new_lower)
