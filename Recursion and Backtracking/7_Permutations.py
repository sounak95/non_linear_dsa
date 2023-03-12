
# https://leetcode.com/problems/permutations/

class Solution(object):
    def helper(self, index, nums, ans):
        if index ==len(nums):
            ans.append(nums.copy())
            return

        for i in range(index, len(nums)):
            nums[index], nums[i] = nums[i], nums[index]
            self.helper(index+1, nums, ans)
            nums[index], nums[i] = nums[i], nums[index]


    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        self.helper(0, nums, ans)
        return ans
