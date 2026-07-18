class Solution:
    def findGCD(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        a = nums[0]
        b = nums[n-1]

        while b:
            a, b = b, a%b
        
        return a
