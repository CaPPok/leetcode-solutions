class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        MOD = 10**9 + 7
        
        dp_sum = [[-1] * n for _ in range(n)]
        dp_cnt = [[0] * n for _ in range(n)]
        
        dp_sum[n-1][n-1] = 0
        dp_cnt[n-1][n-1] = 1
        
        for r in range(n-1, -1, -1):
            for c in range(n-1, -1, -1):
                if board[r][c] == 'X' or (r == n-1 and c == n-1):
                    continue
                
                max_prev = -1
                ways = 0
                
                for dr, dc in [(1, 0), (0, 1), (1, 1)]:
                    pr, pc = r + dr, c + dc
                    
                    if pr < n and pc < n and dp_sum[pr][pc] != -1:
                        if dp_sum[pr][pc] > max_prev:
                            max_prev = dp_sum[pr][pc]
                            ways = dp_cnt[pr][pc]
                        elif dp_sum[pr][pc] == max_prev:
                            ways = (ways + dp_cnt[pr][pc]) % MOD
                            
                if max_prev != -1:
                    val = 0 if board[r][c] in ('E', 'S') else int(board[r][c])
                    dp_sum[r][c] = max_prev + val
                    dp_cnt[r][c] = ways
                    
        if dp_cnt[0][0] == 0:
            return [0, 0]
            
        return [dp_sum[0][0], dp_cnt[0][0]]