# 정확한 순위
N, M = map(int, input().split())

graph = [[0] * N for _ in range(N)]

nodes = []
for _ in range(M):
    u, v = list(map(int, input().split()))
    graph[u - 1][v - 1] = 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if graph[i][j] == 0:
                if graph[i][k] + graph[k][j] > 1:
                    graph[i][j] = 1

result = [0] * N
for i in range(N):

    for j in range(N):
        if graph[i][j] == 1 or graph[j][i]==1:
            result[i] += 1
print(result.count(N-1))


