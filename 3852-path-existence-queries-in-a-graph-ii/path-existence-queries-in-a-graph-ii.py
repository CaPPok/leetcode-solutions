class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        vals = sorted(list(set(nums)))
        m = len(vals)
        
        comp = [0] * m
        for i in range(1, m):
            comp[i] = comp[i-1] + (1 if vals[i] - vals[i-1] > maxDiff else 0)
            
        LOG = 20
        up = [[0] * LOG for _ in range(m)]
        
        right = 0
        for i in range(m):
            while right + 1 < m and vals[right + 1] - vals[i] <= maxDiff:
                right += 1
            up[i][0] = right
            
        for k in range(1, LOG):
            for i in range(m):
                up[i][k] = up[up[i][k-1]][k-1]
                
        val_to_idx = {v: i for i, v in enumerate(vals)}
        
        ans = []
        for u, v in queries:
            if u == v:
                ans.append(0)
                continue
                
            if nums[u] == nums[v]:
                ans.append(1)
                continue
            
            val_u, val_v = min(nums[u], nums[v]), max(nums[u], nums[v])
            s_idx = val_to_idx[val_u]
            e_idx = val_to_idx[val_v]
            
            if comp[s_idx] != comp[e_idx]:
                ans.append(-1)
                continue
                
            curr = s_idx
            steps = 0
            
            for k in range(LOG - 1, -1, -1):
                if up[curr][k] < e_idx:
                    curr = up[curr][k]
                    steps += (1 << k)
            
            ans.append(steps + 1)
            
        return ans