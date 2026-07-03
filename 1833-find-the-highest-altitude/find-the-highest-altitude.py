class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        current = 0

        for i in gain:
            current = current + i
            if current > highest:
                highest = current
        return highest


