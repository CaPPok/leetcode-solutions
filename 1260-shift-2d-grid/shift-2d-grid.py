class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if(k <= 0):
            return grid

        row = len(grid)
        col = len(grid[0])
        n = row * col
        k = k % n

        if(k <= 0):
            return grid

        def shift(i, j):
            while(i < j):
                grid[i // col][i % col], grid[j // col][j % col] = grid[j // col][j % col], grid[i // col][i % col]
                i += 1
                j -= 1

        shift(0, n-1)
        shift(0, k-1)
        shift(k, n-1)

        return grid