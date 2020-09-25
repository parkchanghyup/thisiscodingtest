# 화성 탐사
import heapq

N = int(input())
graph = []
INF = int(1e9)
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

for i in range(N):
    graph.append(list(map(int, input().split())))

# (비용, y, x)
Q = [(graph[0][0], 0, 0)]
result = int(1e9)
while Q:
    weight, y, x = heapq.heappop(Q)

    if y == N - 1 and x == N - 1:
        result = min(result, graph[N - 1][N - 1])
        break

    graph[y][x] = -weight

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny >= 0 and nx >= 0 and ny < N and nx < N and graph[ny][nx] >= 0:
            graph[ny][nx] += weight
            if ny == N-1 and nx == N-1:
                result = graph[ny][nx]

            heapq.heappush(Q, (graph[ny][nx], ny, nx))
    if result != int(1e9):
        break

print(result)
