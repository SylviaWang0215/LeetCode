__author__ = 'mac'


class Solution(object):
    def multiply(self, num1, num2):
        len1 = len(num1) - 1
        len2 = len(num2) - 1

        ans = ""
        temp = ""
        for i in range(len1, -1, -1):
            tens = 0
            for j in range(len2, -1, -1):
                unit = int(num1[i]) * int(num2[j]) + tens
                #print("unit = ", unit)
                tens = int(unit/10)
                unit %= 10
                temp = str(unit) + temp
            if tens != 0:
                temp = str(tens) + temp
            print("temp = ", temp)
            #print(ans)
            lentemp = len(temp) + len1 - 1 - i
            #print("lentemp", lentemp)
            rec = temp
            temp = temp.ljust(lentemp+1)
            temp = temp.replace(" ", "0")

            lenans = len(temp) - 1
            addtens = 0
            if len(ans) == 0:
                ans = rec
            else:
                ans = ans.rjust(len(temp))
                ans = ans.replace(" ", "0")
                print("ans = ", ans, "temp = ", temp)
                for k in range(lenans, -1, -1):


                    addunit = int(temp[k]) + int(ans[k]) + addtens

                    addtens = int(addunit / 10)
                    addunit %= 10
                    ans = ans[:k] + str(addunit) + ans[k+1:]
            #print("new round")
            if addtens != 0:
                ans = str(addtens) + ans
            print("ans = ", ans)
            temp = ""
        return ans

num1 = "123"
num2 = "456"
f = Solution()
print(f.multiply(num1, num2))