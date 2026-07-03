class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        
        adj = [[] for _ in range(n)]
        in_degree = [0] * n
        max_cost = 0
        
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                in_degree[v] += 1
                if cost > max_cost:
                    max_cost = cost
                    
        q = deque()
        for i in range(n):
            if online[i] and in_degree[i] == 0:
                q.append(i)
                
        topo_order = []
        while q:
            u = q.popleft()
            topo_order.append(u)
            for v, _ in adj[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    q.append(v)
                    
        topo_order.reverse()
        
        def isValid(min_limit: int) -> bool:
            dp = [float('inf')] * n
            dp[n - 1] = 0
            
            for u in topo_order:
                for v, cost in adj[u]:
                    if cost >= min_limit:
                        if dp[v] + cost < dp[u]:
                            dp[u] = dp[v] + cost
                            
            return dp[0] <= k

        ans = -1
        left, right = 0, max_cost
        
        while left <= right:
            mid = (left + right) // 2
            if isValid(mid):
                ans = mid        
                left = mid + 1
            else:
                right = mid - 1
                
        return ans