"""
LeetCode #886 : Possible Bipartition
[https://leetcode.com/problems/possible-bipartition/]
Date: April 30 2022
Notes:
    Used bfs, and bipartite graph coloring
"""
from collections import deque
from typing import List

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1] * (n + 1)
        graph = {}
        for e in dislikes:
            a, b = e
            if graph.get(a, None) == None:
                graph[a] = []
            graph[a].append(b)
            if graph.get(b, None) == None:
                graph[b] = []
            graph[b].append(a)

        for i in range(1, n + 1):
            if color[i] != -1:
                continue

            q = deque()
            q.append((i, 0))

            while q:
                node, c = q.popleft()
                if color[node] == -1:
                    color[node] = c
                    for nbors in graph.get(node, []):
                        q.append((nbors, c ^ 1))
                if color[node] != c:
                    return False
        return True



