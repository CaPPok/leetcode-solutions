class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: list[list[int]]) -> int:
        row_map = {}
        for row, seat in reservedSeats:
            if row not in row_map:
                row_map[row] = set()
            row_map[row].add(seat)
            
        max_families = 2 * n
        
        for row, seats in row_map.items():
            left_free = True
            right_free = True
            mid_free = True
            
            if any(s in seats for s in [2, 3, 4, 5]):
                left_free = False
                
            if any(s in seats for s in [6, 7, 8, 9]):
                right_free = False
                
            if any(s in seats for s in [4, 5, 6, 7]):
                mid_free = False
                
            if left_free and right_free:
                continue
            elif left_free or right_free or mid_free:
                max_families -= 1
            else:
                max_families -= 2
                
        return max_families