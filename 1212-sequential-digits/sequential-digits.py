class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        s = "123456789"
        l = str(low)
        h = str(high)

        for i in range(len(l), len(h)+1):
            for j in range(10-i):
                num = int(s[j:j+i])
                if (low <= num <= high):
                    ans.append(num)

        return ans
        