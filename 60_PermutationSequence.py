__author__ = 'mac'
class Solution(object):
    def getPermutation(self, n, k):
        lis = []
        nums = list(range(1, n+1))
        if nums is []:
            return []
        length = len(nums)
        temp = [[nums[length - 1]]]
        if length == 1:
            return temp
        count = 1
        times = 1
        for i in range(length-2, -1, -1):
            lis = []
            for l in range(count):
                for j in range(times + 1):
                    temp_lis = temp[l][:]
                    temp_lis.insert(j, nums[i])
                    lis.append(temp_lis)
            count *= (times + 1)
            times += 1
            temp = lis
        lis.sort()
        temp_ans = lis[k-1]
        ans = "".join(str(x) for x in temp_ans)
        return ans