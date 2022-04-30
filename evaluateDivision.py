"""
LeetCode #399 : Evaluate Division
[https://leetcode.com/problems/evaluate-division/]
Date: April 30 2022
Notes:
    Used dfs
"""

from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        def populateNode(edge, value, graph):
            retList = []
            if edge[0] not in graph:
                graph[edge[0]] = {'nbors': [], 'wts': []}
            graph[edge[0]]['nbors'].append(edge[1])
            graph[edge[0]]['wts'].append(value)

            if edge[1] not in graph:
                graph[edge[1]] = {'nbors': [], 'wts': []}
            graph[edge[1]]['nbors'].append(edge[0])
            graph[edge[1]]['wts'].append(1.0 / value)
            return graph

        def dfs(node, cost, dest, visited, graph):
            if node == dest:
                return cost
            if len(visited) == len(graph):
                return -1
            for i, n in enumerate(graph[node]['nbors']):
                if n not in visited:
                    newcost = dfs(n, graph[node]['wts'][i], dest, visited + [n], graph)
                    if newcost < 0:
                        continue
                    return cost * newcost
            return -1

        graph = {}
        for i, v in enumerate(equations):
            src, dest = v
            graph = populateNode(v, values[i], graph)

        results = []
        for v in queries:
            a, b = v
            if (a not in graph.keys()) or (b not in graph.keys()):
                results.append(-1.)
            else:
                cost = dfs(a, 1, b, [a], graph)
                if cost < 0:
                    results.append(-1.)
                else:
                    results.append(cost)

        return results

