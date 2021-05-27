class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        r, c = len(maze), len(maze[0])
        pq = [(0, start[0], start[1])]
        processed = {(start[0], start[1]): 0}
        
        while pq:
            dist, x, y = heapq.heappop(pq)
            if [x, y] == destination:
                return dist
            
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_r, new_c, d = x, y, 0
                
                while 0 <= new_r + i < r and 0 <= new_c + j < c and maze[new_r + i][new_c + j] != 1:
                    new_r += i
                    new_c += j
                    d += 1
                    
                if (new_r, new_c) not in processed or dist + d < processed[(new_r, new_c)]:
                    processed[(new_r, new_c)] = dist + d
                    heapq.heappush(pq, (dist + d, new_r, new_c))
                    
        return -1
