class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = [[] for _ in range(n+1)]
        for i in roads:
            adj[i[0]].append((i[1], i[2]))
            adj[i[1]].append((i[0], i[2]))
        
        visit = [False]*(n+1)
        q = deque([1])
        visit[1] = True

        ans = float('inf')

        while q:
            u = q.popleft()

            for v, w in adj[u]:
                if(w < ans):
                    ans = w
                
                if not visit[v]:
                    visit[v] = True
                    q.append(v)

        return ans

