class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c: str) -> bool:
            vw = ['a','e','i','o','u']
            VW = ['A','E','I','O','U']
            if (c in vw or c in VW):
                return True
            return False

        listS = []
        m = len(s)
        l = 0
        r = m - 1

        for i in range(m):
            listS.append(s[i])

        while(l < r):
            if(isVowel(s[l]) == False):
                l += 1
            elif(isVowel(s[r]) == False):
                r -= 1
            else:
                listS[l], listS[r] = listS[r], listS[l]
                l += 1
                r -= 1
                
        
        ans = ""
        for i in range(m):
            ans = ans + listS[i]

        return ans
