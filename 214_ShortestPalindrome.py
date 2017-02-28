__author__ = 'mac'


class Solution():
    def shortestPalindrome(self, s):
        length = len(s)
        start_index = 0
        longest_sub = ""
        if length <= 0:
            return s
        reverse_s = s[::-1]
        while reverse_s[start_index:length].find(s[0]) != -1:
            reverse_index = reverse_s[start_index:length].index(s[0])
            print("reverse_index", reverse_index)
            end_index = length - reverse_index - start_index - 1
            print("start_index", start_index)
            #print(length - reverse_index + start_index)
            print("end index = ", end_index)
            sub = s[:end_index+1]
            forward_string = sub
            backward_string = sub[::-1]
            print("forward_string", forward_string)
            print("backward_string", backward_string)
            if forward_string == backward_string:
                longest_sub = sub
                print("longest_sub", longest_sub)
                sub_length = len(longest_sub)
                temp = s[sub_length::]
                temp = temp[::-1]
                return temp + s
            start_index = reverse_index + start_index + 1
        if longest_sub == "":
            temp = s[1::]
            temp = temp[::-1]
        return temp + s


s1 = "aacecaaa"
s2 = "a"
s3 = "abcd"
s4 = "aba"
s5 = "xabay"
s6 = "abbabaab"
f = Solution()
print(f.shortestPalindrome(s5))