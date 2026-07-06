class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if(n <= 1):
            return n
        
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        maxL = 0

        for i in intervals:
            if i[1] > maxL:
                count += 1
                maxL = i[1]

        return count

