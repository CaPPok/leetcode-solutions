class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        sum = 0
        mul = 1

        while (n > 0):
            d = n % 10
            if (d != 0):
                x = d * mul + x
                mul *= 10
                sum += d

            n = n // 10
        return x*sum
        