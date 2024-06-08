from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {v:[] for v in range(numCourses)}
        indegree = [0] * numCourses

        for a,b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        q = deque()
        for n, v in enumerate(indegree):
            if v == 0:
                q.append(n)
        
        while q:
            cur_n = q.popleft()
            for node in graph[cur_n]:
                indegree[node] -= 1
                if indegree[node] == 0:
                    q.append(node)

        return all(n == 0 for n in indegree)        