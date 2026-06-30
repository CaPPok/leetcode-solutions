from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = defaultdict(int)
        operations = 0
        
        for num in nums:
            target = k - num
            if seen[target] > 0:
                operations += 1
                seen[target] -= 1
            else:
                seen[num] += 1
                
        return operations