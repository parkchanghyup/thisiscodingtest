# 이것이 코딩테스트다 - 정수 삼각형

from typing import List
def soltuion(N: int, numbers: List):

    for i in range(1, N):
        for j in range(len(numbers[i])):

            if j == 0:
                numbers[i][j] += numbers[i-1][j]
            elif j == len(numbers[i])-1:
                numbers[i][j] += numbers[i-1][j-1]
            else:
                numbers[i][j] += max(numbers[i-1][j], numbers[i-1][j-1])

    return max(numbers[N-1])


n = int(input())
numbers = []
for i in range(n):
    numbers.append(list(map(int, input().split())))

print(soltuion(N, numbers))