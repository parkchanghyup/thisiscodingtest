# 이것이 코딩테스트다 - 전보 (최단경로) 
import collections
import heapq
start = 1
nodes = [[1,2,4],[1,3,2]]

#그래프 생성
graph = collections.defaultdict(list)
for u,v,w in nodes:
    graph[u].append((v,w))

Q = [(0,start)]
dist = collections.defaultdict(list)

while Q:
    d,node = heapq.heappop(Q)
    
    if node not in dist:
        dist[node] =d
        
        for v,w in graph[node]:
            heapq.heappush(Q,(w+d,v))

print(len(dist)-1,max(dist.values()))
