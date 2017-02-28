__author__ = 'mac'
#use stack?


class Solution(object):
    def longestValidParenthese(self, s):
        l = len(s)
        count = 0
        temp = ''
        for i in range(l):
            if s[i] == '(' & temp != '(':
                count += 1
                temp = '('
            else:
                if i == 0:
                    count = 0
                elif temp == '(':
                    count += 1
                    temp = ')'
                else:
                    count = 0
            return count

s1 = '(()'
s2 = '()(()()'
f = Solution()
print(f.longestValidParenthese(s1))