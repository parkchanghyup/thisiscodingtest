# 이것이 코딩 테스트다 - 안테나 (정렬)

import sys

N = int(input())

house = list(map(int, input().split()))

house.sort()

print(house[(len(house) - 1) // 2])