__author__ = 'mac'


class Solution(object):
    def permute(self, nums):
        lis = []
        if nums == []:
            return []
        length = len(nums)
        temp = [[nums[length - 1]]]
        if length == 1:
            return temp
        count = 1
        times = 1
        for i in range(length-2, -1, -1):
            lis = []
            for k in range(count):
                for j in range(times + 1):
                    temp_lis = temp[k][:]
                    temp_lis.insert(j, nums[i])
                    lis.append(temp_lis)
            count *= (times + 1)
            times += 1
            temp = lis
        return lis

s1 = [1, 2, 3]
f = Solution()
ans = f.permute(s1)
ans.sort()
print(ans)
#print "final answer = ", f.permute(s1)