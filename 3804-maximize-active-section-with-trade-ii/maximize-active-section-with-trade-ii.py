class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        N = len(s)
        total_ones = s.count('1')
        
        starts = []
        ends = []
        left_bounds = []
        right_bounds = []
        
        i = 0
        zero_start = -1
        while i < N:
            if s[i] == '0':
                zero_start = i
                while i < N and s[i] == '0':
                    i += 1
            else:
                one_start = i
                while i < N and s[i] == '1':
                    i += 1
                starts.append(one_start)
                ends.append(i - 1)
                
                if one_start > 0:
                    left_bounds.append(zero_start)
                else:
                    left_bounds.append(one_start)
        
        M = len(starts)
        for j in range(M):
            if ends[j] < N - 1:
                if j + 1 < M:
                    right_bounds.append(starts[j+1] - 1)
                else:
                    right_bounds.append(N - 1)
            else:
                right_bounds.append(ends[j])
                
        full_gains = []
        for j in range(M):
            gain = (starts[j] - left_bounds[j]) + (right_bounds[j] - ends[j])
            full_gains.append(gain)
            
        st = []
        if M > 0:
            LOG = M.bit_length()
            st = [[0] * M for _ in range(LOG)]
            st[0] = full_gains[:]
            for j in range(1, LOG):
                length = 1 << j
                half = 1 << (j - 1)
                for k in range(M - length + 1):
                    st[j][k] = max(st[j-1][k], st[j-1][k + half])
        
        def query_st(l, r):
            if l > r: return 0
            j = (r - l + 1).bit_length() - 1
            return max(st[j][l], st[j][r - (1 << j) + 1])
            
        ans = []
        for L, R in queries:
            idx_L = bisect.bisect_right(starts, L)
            idx_R = bisect.bisect_left(ends, R) - 1
            
            max_gain = 0
            if idx_L <= idx_R:
                if idx_L == idx_R:
                    gain = (starts[idx_L] - max(L, left_bounds[idx_L])) + (min(R, right_bounds[idx_L]) - ends[idx_L])
                    max_gain = gain
                else:
                    first = idx_L
                    last = idx_R
                    
                    g_first = (starts[first] - max(L, left_bounds[first])) + (right_bounds[first] - ends[first])
                    g_last = (starts[last] - left_bounds[last]) + (min(R, right_bounds[last]) - ends[last])
                    g_mid = query_st(first + 1, last - 1)
                    
                    max_gain = max(g_first, g_last, g_mid)
                    
            ans.append(total_ones + max_gain)
            
        return ans