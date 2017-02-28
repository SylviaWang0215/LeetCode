__author__ = 'mac'


class Solution(object):
    def reconstructQueue(self, people):
        #people.sort()
        #people = sorted(people, key=lambda x:x[1])
        print people
        length = len(people)
        dic = {}
        res = []
        for i in range(length):
            item = people[i]
            if item[0] in dic:
                dic[item[0]] += (item[1], i),
            else:
                dic[item[0]] = [(item[1], i)]
        key_list = dic.keys()
        key_list.sort()
        print dic
        #the number of the height that is taller or same as the item[i] will be the
        #index of item[i] is we sort them from the highest one
        for i in key_list[::-1]:
            dic[i].sort()
            for p in dic[i]:
                print p[0], people[p[1]]
                res.insert(p[0], people[p[1]])
                print res
        print res



people1 = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
f = Solution()
f.reconstructQueue(people1)
