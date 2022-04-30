"""
LeetCode #785 : Is Graph Bipartite
[https://leetcode.com/problems/is-graph-bipartite/]
Date: April 29 2022
Notes:
    Watched solution on https://www.youtube.com/watch?v=CscLi1gVGUk&ab_channel=TimothyHChang
    Used bipartite graph coloring via bfs
"""
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        N = len(graph)
        col = [-1] * N

        for i in range(N):
            print(i)
            if col[i] != -1:
                continue
            q = deque()
            q.append((i, 0))

            while q:
                node, color = q.popleft()
                print(node, color)
                if col[node] == -1:
                    col[node] = color
                    for nbors in graph[node]:
                        q.append((nbors, color ^ 1))
                if col[node] != color:
                    return False
        return True
