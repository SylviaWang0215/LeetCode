__author__ = 'mac'


class Solution(object):
    def DFS(self, candidate, target, start, valuelist):
        length = len(candidate)
        if target == 0:
            return Solution.ret.append(valuelist)
        for i in range(start, length):
            if valuelist == [] and i != 0 and candidate[i] == candidate[i - 1]:
                continue
            if target < candidate[i]:
                return
            self.DFS(candidate, target - candidate[i], i+1, valuelist+[candidate[i]])

    def combinationSum2(self, candidates, target):
        new_candidates = [x for x in candidates if x <= target]
        new_candidates.sort()
        Solution.ret = []
        self.DFS(new_candidates, target, 0, [])
        return Solution.ret
