
# https://leetcode.com/problems/combination-sum-ii/

class Solution(object):

    def helper(self,ind, target, arr, ans, ds):

        if target==0:
            ans.append(ds.copy())
            return

        for i in range(ind, len(arr)):
            if i>ind and arr[i]==arr[i-1]:
                continue
            if arr[i]>target:
                break
            ds.append(arr[i])
            self.helper(i+1, target-arr[i], arr, ans, ds)
            ds.pop()



    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ds=[]
        ans=[]
        candidates.sort()
        self.helper(0,  target, candidates, ans, ds)
        return ans



candidates =[10,1,2,7,6,1,5]
target=8

print(Solution().combinationSum2(candidates, target))