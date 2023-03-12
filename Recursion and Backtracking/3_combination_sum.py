
# https://leetcode.com/problems/combination-sum/

class Solution(object):

    def helper(self, index, ds, candidates, target, ans):
        if index == len(candidates):
            if target==0:
                ans.append(ds.copy())
            return


        if candidates[index]<=target:
            ds.append(candidates[index])
            self.helper(index, ds, candidates, target-candidates[index], ans)
            ds.pop()

        self.helper(index+1, ds, candidates, target, ans)

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans=[]
        ds=[]
        index=0
        self.helper(index,ds, candidates, target, ans)
        return ans

print(Solution().combinationSum([2,3,6,7], 7))