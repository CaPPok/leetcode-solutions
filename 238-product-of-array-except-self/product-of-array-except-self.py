class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1]*n
        cur = 1

        for i in range(n):
            ans[i] = ans[i] * cur
            cur = cur * nums[i]
        
        cur = 1
        for i in range(n-1,-1,-1):
            ans[i] = ans[i] * cur
            cur = cur * nums[i]

        return ans