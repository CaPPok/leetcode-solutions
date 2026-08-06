class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def productDigits(n):
            product = 1
            while n:
                product *= n % 10
                n //= 10

            return product
        
        while(productDigits(n) % t != 0):
            n += 1
            
        return n