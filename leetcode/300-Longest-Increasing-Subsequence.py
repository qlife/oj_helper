class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        lis_len = [1] * n

        for k in range(n):
            for i in range(k):
                if nums[i] < nums[k]:
                    lis_len[k] = max(lis_len[k], 1 + lis_len[i])

        return max(lis_len)