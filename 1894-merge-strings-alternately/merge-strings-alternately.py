class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = []
        min_length = min(len(word1), len(word2))
        
        for i in range(min_length):
            ans.append(word1[i])
            ans.append(word2[i])
            
        if(len(word1) > min_length):
            ans.append(word1[min_length:])
        else:
            ans.append(word2[min_length:])
        
        return "".join(ans)