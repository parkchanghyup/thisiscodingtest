# 이것이 코딩테스트다 - 게임 개발 (구현)

n, m = 4, 4
graph = [[0] * n for _ in range(m)]

#현재 캐릭터의 좌표  #북: 0 , 동 :1 , 남 :2 , 서 :3
x, y, pos = 1, 1, 0

map_list = [1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1]

# 맵 생성
for i in range(n):
    for j in range(m):
        graph[i][j] = map_list[i * 4 + j]
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, +1]
count = 0

while True:

    count += 1
    graph[x][y] = 1

    if pos < 0: pos += 4

    possible = False

    for i in range(0, 4):
        # 갈수있으면
        if graph[x + dx[i]][y + dy[i]] == 0:
            pos = pos - i - 1
            x += dx[i]
            y += dy[i]
            #갈곳이 있다.
            possible = True
            break

    if possible: continue

    if graph[x - dx[pos]][y - dx[pos]] == 0:
        x += dx[back_pos]
        y += dy[back_pos]
    else:
        break

print(count)



'''
# N, M을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    #direction 전역변수
    global_direction 
    direction -= 1
    if direction ==-1:
        direction =3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    
    #왼쪽으로 회전 
    turn_left()
    nx = x +dx[directions]
    ny = y +dy[directions]
    
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if d[nx][ny] ==0 and array[nx][ny]==0:
        d[nx][ny] =1
        x = nx
        y= ny
        count +=1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else :
        turn_time +=1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time = 4:
        nx = x-dx[direction]
        ny = y-dy[direction]
        # 뒤로 갈 수 있다면 이동
        if array[nx][ny] ==0:
            x = nx
            y= ny
        #뒤가 바다로 막혀있다면 
        else:
            break
        turn_time = 0

#정답 출력
print(count)
        
        '''