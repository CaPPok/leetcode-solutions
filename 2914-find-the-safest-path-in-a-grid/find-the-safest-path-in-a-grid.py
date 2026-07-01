class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
            
        dist = [[-1] * n for _ in range(n)]
        q = deque()
        
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    q.append((r, c))
                    dist[r][c] = 0
                    
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))
                    
        def isValid(safe_limit):
            if dist[0][0] < safe_limit:
                return False
                
            visited = [[False] * n for _ in range(n)]
            bq = deque([(0, 0)])
            visited[0][0] = True
            
            while bq:
                r, c = bq.popleft()
                if r == n - 1 and c == n - 1:
                    return True
                    
                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                        if dist[nr][nc] >= safe_limit:
                            visited[nr][nc] = True
                            bq.append((nr, nc))
            return False

        left, right = 0, n * 2
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if isValid(mid):
                ans = mid      
                left = mid + 1  
            else:
                right = mid - 1
                
        return ans