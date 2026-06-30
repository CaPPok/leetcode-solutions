class Solution:
    def gcd(n1: int, n2: int) -> int:
        if(n1 == n2):
            return n1
        
        if(n1 > n2):
            return gcd(n1-n2, n2)
        else:
            return gcd(n1, n2-n1)
        
        return 0
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        
        l1 = len(str1)
        l2 = len(str2)
        gcdStr = gcd(l1,l2)
        return str1[:gcdStr]  

        