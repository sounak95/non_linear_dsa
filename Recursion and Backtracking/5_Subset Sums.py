
# https://practice.geeksforgeeks.org/problems/subset-sums2234/1


class Solution:
    def helper(self, index, arr, N, sum,ans):
        if index==N:
            ans.append(sum)
            return

        self.helper(index+1, arr, N, sum+arr[index], ans)
        self.helper(index + 1, arr, N, sum , ans)

    def subsetSums(self, arr, N):
        sum=0
        ans=[]
        self.helper(0,arr,N, 0,ans)
        return sorted(ans)

