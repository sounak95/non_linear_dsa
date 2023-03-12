



class Solution(object):

    def helper(self, index, sum, nums,  target):
        if index==len(nums):
            if sum == target:
                return 1
            return 0

        sum+=nums[index]
        left = self.helper(index+1, sum, nums, target)
        sum-=nums[index]
        right = self.helper(index+1, sum, nums, target)

        return left+right

    def numSubseq(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        return self.helper(0,0,nums, target)

print(Solution().numSubseq([1,1,2],3))
