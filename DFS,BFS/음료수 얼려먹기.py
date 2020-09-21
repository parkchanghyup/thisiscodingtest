# 이것이 코딩테스트다 - 음료수 얼려먹기 (BFS/DFS)
ice = ['00110', '00011', '11111', '00000']
graph = [[i for i in ice_list] for ice_list in ice]
graph

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(graph, y, x):
    
    graph[y][x] = '1'
    print(y, x)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx > -1 and nx < 5 and ny > -1 and ny < 4:
            if graph[ny][nx] == '0':
                dfs(graph, ny, nx)


count = 0

for i in range(4):
    for j in range(5):
        if graph[i][j] == str(0):
            dfs(graph, i, j)
            print('')
            count += 1

print(count)


'''
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력
'''