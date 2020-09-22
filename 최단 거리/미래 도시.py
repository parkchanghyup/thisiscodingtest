# 이것이 코딩테스트다 - 미래 도시 (최단경로) 

# 1번회사에서 출발 하여 K번 회사를 방문한 뒤에 X번 회사로 가는 것이 목표.
INF = int(1e9)


n,X ,K= 5,4,5
nodes = [[1,2],[1,3],[1,4],[2,4],[3,4],[3,5],[4,5]]

# 2차원 리스트 생성후 무한으로 초기화
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기자신에게 가는 비용 0으로 초기화
for i in range(1,6):
    for j in range(1,6):
        if i==j : graph[i][j] = 0

#  간선 정보 입력

for node in nodes:
    graph[node[0]][node[1]] =1
    graph[node[1]][node[0]] = 1
    
#플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
result = graph[1][K] + graph[K][X]

print(result)
