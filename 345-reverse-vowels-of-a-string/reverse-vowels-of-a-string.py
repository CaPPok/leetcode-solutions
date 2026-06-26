class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = []
        for i in s:
            if(i in "aeiouAEIOU"):
                vowels.append(i)

        ans = []
        for i in s:
            if(i not in "aeiouAEIOU"):
                ans.append(i)
            else:
                ans.append(vowels.pop())

        return "".join(ans)
                