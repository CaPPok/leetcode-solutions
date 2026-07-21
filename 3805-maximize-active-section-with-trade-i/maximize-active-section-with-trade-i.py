class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        initial_ones = s.count('1')
        s = '1' + s + '1'
        n = len(s)
        i = 0
        max_active = initial_ones

        while i < n and s[i] == '1':
            i += 1

        left_zeros = 0
        while i < n and s[i] == '0':
            left_zeros += 1
            i += 1

        while i < n:
            mid_ones = 0
            while i < n and s[i] == '1':
                mid_ones += 1
                i += 1

            if mid_ones == 0:
                break

            right_zeros = 0
            while i < n and s[i] == '0':
                right_zeros += 1
                i += 1

            if right_zeros == 0:
                break

            max_active = max(max_active, initial_ones + left_zeros + right_zeros)
            
            left_zeros = right_zeros

        return max_active