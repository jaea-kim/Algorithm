import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {v:[] for v in range(1, n+1)}
        for u, v, w in times:
            nodes = graph.get(u, [])
            nodes.append((w, v))
            graph[u] = nodes

        visited = [False] * n 
        distance = {v:float("inf") for v in graph}
        distance[k] = 0
        visited[k-1] = True
        q = []
        heapq.heappush(q, (0, k))

        while q:
            cur_c, cur_n = heapq.heappop(q)
            if distance[cur_n] < cur_c:
                continue
            
            for cost, next_n in graph[cur_n]:
                next_c = distance[cur_n] + cost
                if next_c < distance[next_n]:
                    distance[next_n] = next_c
                    visited[next_n - 1] = True
                    heapq.heappush(q, (next_c, next_n))

        if all(visited):
            return max(distance.values())

        return -1