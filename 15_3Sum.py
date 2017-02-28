__author__ = 'mac'

class Solution(object):
    def threeSum(self, nums):
        length = len(nums)
        nums = sorted(nums)
        neg = [x for x in nums if x < 0]
        pos = [x for x in nums if x >= 0]
        length_neg = len(neg)
        length_pos = len(pos)
        i = 0
        lis = []
        used = []
        if length <= 2 or nums[0] > 0 or nums[length - 1] < 0:
            return []
        if pos[2] == 0:
            lis.append([0, 0, 0])
        while i < length_neg:
            j = i + 1
            while j < length_neg:
                temp_sum = neg[i] + neg[j]
                if -temp_sum in pos and [neg[i], neg[j]] not in used:
                    lis.append([neg[i], neg[j], -temp_sum])
                    used.append([neg[i], neg[j]])
                j += 1
            i += 1

        i = 0

        while i < length_pos:
            j = i + 1
            while j < length_pos:
                temp_sum = pos[i] + pos[j]
                if -temp_sum in neg and [pos[i], pos[j]] not in used:
                    lis.append([-temp_sum, pos[i], pos[j]])
                    used.append([pos[i], pos[j]])
                j += 1
            i += 1
        lis = sorted(lis)
        return lis

s1 = [-1, 0, 1, 2, -1, -4]
s2 = [0, 0]
s3 = [-14,-10,-1,8,-8,-7,-3,-2,14,10,3,3,-1,-15,6,9,-1,6,-2,-6,-8,-15,8,-3,-14,5,-1,-12,-10,-5,-9,-8,1,-3,-15,0,-3,-11,6,-11,7,-6,7,-9,-6,-10,7,1,11,-10,10,-12,-10,3,-7,-9,-7,7,-14,-9,10,14,-2,-4,-4,-10,3,1,-14,-6,5,8,-4,-11,14,-3,-6,-2,13,13,3,0,-14,8,10,-14,6,11,1,7,-13,-4,6,0,-1,10,-3,-13,-4,-2,-11,8,-8]
s4 = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
f = Solution()
print(f.threeSum(s4))