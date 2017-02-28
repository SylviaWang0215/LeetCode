__author__ = 'mac'


class Solution(object):
    def generateParenthesis(self, n):
        temp = [["(", [1, 0]]]
        dic = []
        count_right = 0
        if n == 0:
            return [""]
        while count_right <= n:
            count = 0
            for item in temp:
                key = item[0]
                lis = item[1]
                count_left = lis[0]
                count_right = lis[1]
                if count_right == n:
                    count += 1
                    if count == len(temp):
                        ans = [x[0] for x in temp]
                        return ans
                elif count_left == n and count_right < n:
                    new_str = key + ")"
                    dic.append([new_str, [count_left, count_right + 1]])
                elif count_right == count_left:
                    new_str = key + "("
                    dic.append([new_str, [count_left + 1, count_right]])
                else:
                    new_str1 = key + "("
                    new_str2 = key + ")"
                    dic.append([new_str1, [count_left + 1, count_right]])
                    dic.append([new_str2, [count_left, count_right + 1]])
            temp = dic
            dic = []

n1 = 3
f = Solution()
#f.generateParenthesis(n1)
print(f.generateParenthesis(n1))



