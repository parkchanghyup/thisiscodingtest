# 이것이 코딩 테스트다 - 플로이드 ( 최단 경로 문제)

from typing import List
ㅠㅠㅠ

def solution(N: int, K: int, loads: List):
    graph = [[1e9]*N for _ in range(N)]
    
    for u, v, w in loads:
        if graph[u-1][v-1] > w:
            graph[u-1][v-1] = w
    
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    graph[i][j] = 0
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    print(graph)

N = int(input())
M = int(input())
load = list(map(int, input().split()))


loads = []
for i in range(0, len(load), 3):
    loads.append(load[i:i+3])
solution(N, M, loads)