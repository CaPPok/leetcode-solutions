class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        setnums = set(nums)
        ans = k

        while ans in setnums:
            ans += k

        return ans