class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        l = 0
        ones = 0

        for r in range(len(s)):
            if s[r] == '1':
                ones += 1

            while ones > k:
                if s[l] == '1':
                    ones -= 1
                l += 1

            while ones == k and s[l] == '0':
                l += 1

            if ones == k:
                candidate = s[l:r + 1]

                if (
                    not ans
                    or len(candidate) < len(ans)
                    or (len(candidate) == len(ans) and candidate < ans)
                ):
                    ans = candidate

        return ans