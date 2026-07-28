class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        if(n <= 1):
            return s
        
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        mid = ""
        if(n % 2 == 1):
            mid = s[n//2]

        l = []
        for i in range(26):
            l.append(chr(ord('a') + i) * (freq[i] // 2))
        
        l = "".join(l)
        r = l[::-1]
        
        return l + mid + r