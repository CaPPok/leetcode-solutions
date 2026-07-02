class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        
        min_cost = [[float('inf')] * n for _ in range(m)]
        
        start_cost = grid[0][0]
        if start_cost >= health:
            return False
            
        min_cost[0][0] = start_cost
        q = deque([(0, 0)])
        
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while q:
            r, c = q.popleft()
            c_cost = min_cost[r][c]
            
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = c_cost + grid[nr][nc]
                    
                    if new_cost < min_cost[nr][nc]:
                        min_cost[nr][nc] = new_cost
                        
                        if grid[nr][nc] == 0:
                            q.appendleft((nr, nc))
                        else:
                            q.append((nr, nc))
                            
        return min_cost[m-1][n-1] < health