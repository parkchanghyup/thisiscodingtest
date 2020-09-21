# 이것이 코딩테스트다 - 상하좌우(구현)

n = 5
move = ['R', 'R', 'R', 'U', 'D', 'D']

position = [1, 1]

for c in move:
    if c == 'R' and position[1] + 1 <= 5:

        position[1] += 1
    elif c == 'L' and position[1] - 1 > 0:
        position[1] -= 1

    elif c == 'U' and position[0] - 1 > 0:
        position[0] -= 1
    elif c == 'D' and position[0] + 1 < 6:
        position[0] += 1

print(position)
'''
# N 입력받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny

print(x, y)
'''