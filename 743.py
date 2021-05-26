class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        pq = [(0, k)]
        dist = {k:0}
        
        while pq:
            d, node = heapq.heappop(pq)            
            for nbr, w in graph[node]:
                if nbr not in dist or dist[nbr] > d + w:
                    dist[nbr] = d + w
                    heapq.heappush(pq,(d + w, nbr))
  
        return max(dist.values()) if len(dist) == n else -1
