class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        maxCandy = candies[0]
        for i in range(1,len(candies)):
            if(candies[i] > maxCandy):
                maxCandy = candies[i]

        for i in range(len(candies)):
            if(candies[i] + extraCandies >= maxCandy):
                ans.append(True)
            else:
                ans.append(False)

        return ans

        