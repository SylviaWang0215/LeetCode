class Solution:
    def twoSum(self, nums, target):
        ans = []
        l = len(nums)
        for i in xrange(l):
            x = nums[i]
            for j in range(i+1, l):
                y = nums[j]
                if x+y == target:
                    ans.append(i)
                    ans.append(j)
                    return ans

test1 = [2, 7, 11, 15]
tar = 9

f = Solution()
print(f.twoSum(test1, tar))

