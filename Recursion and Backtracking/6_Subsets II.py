
# https://leetcode.com/problems/subsets-ii/


class Solution(object):

    def helper(self, index, nums, ds,ans):
        ans.append(ds.copy())

        for i in range(index, len(nums)):
            if i>index and nums[i]==nums[i-1]:
                continue
            ds.append(nums[i])
            self.helper(i+1,nums, ds, ans)
            ds.pop()

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        ds=[]
        nums.sort()
        self.helper(0,nums, ds, ans)
        return ans