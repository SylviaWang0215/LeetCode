__author__ = 'mac'


class Solution():
    def longestPalindrome(self, s):
        length = len(s)-1
        end_index = 0
        i = 0
        longest_sub = ""
        longest_len = 0
        if length == 0 or length == -1:
            return s
        while i < length:
            temp = i
            while s[temp+1:].find(s[i]) != -1:
                end_index = s[temp+1:].index(s[i]) + temp + 1
                sub = s[i: end_index+1]
                len_sub = int(round((len(sub) + 0.0)/2))
                forward_string = sub
                backward_string = sub[::-1]
                print("forward_string = ", forward_string)
                print("backward_string = ", backward_string)
                if forward_string == backward_string:
                    current_length = len(sub)
                    if current_length >= longest_len:
                        longest_len = current_length
                        longest_sub = sub
                temp = end_index
            i += 1
            if len(s[i:]) < longest_len:
                return longest_sub
        if longest_sub == "":
            return s[length]
        return longest_sub

s1 = "babad"
s2 = "cbbd"
s3 = "a"
s4 = "abcdeecba"
s5 = "abcde"
f = Solution()
print(f.longestPalindrome(s5))