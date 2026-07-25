class Solution:
    def maxProduct(self, n: int) -> int:
        max1 = 0
        max2 = 0

        while(n):
            temp = n % 10
            if(temp >= max1):
                max2 = max1
                max1 = temp
            elif(temp > max2):
                max2 = temp    
            n //= 10
        
        return max1 * max2        