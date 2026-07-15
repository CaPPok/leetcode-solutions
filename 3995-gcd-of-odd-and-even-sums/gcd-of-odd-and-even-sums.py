class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        return n
        
        # Sum of the first 4 odd numbers: odd = 1 + 3 + 5 + ... + 2n-1 = n*n
        # Sum of the first 4 even numbers: even = 2 + 4 + 6 + ... + 2n = n(n+1)
        # gcd(n*n, n(n+1)) = n*gcd(n, n+1) = n*1 = n