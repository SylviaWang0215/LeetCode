__author__ = 'mac'


class Solution(object):
    def frequencySort(self, s):
        if not s:
            return ""
        dic = {}
        length = len(s)
        for i in range(length):
            value = s[i]
            if value in dic:
                dic[value] += 1
            else:
                dic[value] = 1
        sorted_dic = sorted(dic.items(), key=lambda x: x[1])
        sorted_dic.reverse()
        print sorted_dic
        keys = [x[0] for x in sorted_dic]
        str = ""
        for item in keys:
            str += item * dic[item]
        return str

str1 = "tree"
str2 = "cccaaa"
str3 = "Aabb"
f = Solution()
print(f.frequencySort(str3))