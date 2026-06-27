class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_len = 1
        
        if 1 in count:
            c = count[1]
            max_len = max(max_len, c if c % 2 == 1 else c - 1)
            
        for x in count:
            if x == 1:
                continue
            
            curr_x = x
            curr_len = 0
            
            while count[curr_x] > 1:
                curr_len += 2
                curr_x *= curr_x

            if count[curr_x] > 0:
                curr_len += 1
            else:
                curr_len -= 1
                
            max_len = max(max_len, curr_len)
            
        return max_len