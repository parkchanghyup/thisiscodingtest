# 숨바꼭질

import sys
import heapq
import collections

N, M = map(int, sys.stdin.readline().split())

graph = collections.defaultdict(list)

INF = int(1e9)

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

dist = collections.defaultdict(int)


def dijkstra(start):
    Q = [(0, start)]


    while Q:
        time, node = heapq.heappop(Q)

        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                heapq.heappush(Q,(w + time, v))


dijkstra(1)
result = []
cnt = 0
max_cnt = -1
for i in range(1,N+1):
    if dist[i] > max_cnt:
        result = [i,dist[i]]
        max_cnt = dist[i]
        cnt =1
    elif dist[i] == max_cnt:
        cnt +=1

print(result[0],result[1],cnt)