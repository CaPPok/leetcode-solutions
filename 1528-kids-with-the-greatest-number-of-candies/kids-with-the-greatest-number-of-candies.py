class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        length = len(candies)
        ans = [False]*length
        maxCandy = candies[0]
        for i in range(1,length):
            if(candies[i] > maxCandy):
                maxCandy = candies[i]

        for i in range(length):
            if(candies[i] + extraCandies >= maxCandy):
                ans[i] = True

        return ans

        