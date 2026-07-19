class Solution:
    def smallestSubsequence(self, s: str) -> str:
        freq = [0]*26
        flag = [False]*26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        ans = []

        for c in s:
            i = ord(c) - ord('a')
            freq[i] -= 1

            if(flag[i]):
                continue
            
            while(ans and ans[-1] > c and freq[ord(ans[-1]) - ord('a')] > 0):
                flag[ord(ans[-1]) - ord('a')] = False
                ans.pop()

            ans.append(c)
            flag[i] = True
        
        return "".join(ans)