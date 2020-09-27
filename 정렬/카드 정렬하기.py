# 이것이 코딩 테스트다 - 카드 정렬하기 (정렬)
import sys
import heapq

N = int(input())

card = []

for _ in range(N):
    num = int(input())
    heapq.heappush(card, num)

result = 0

while len(card) > 1:
    first = heapq.heappop(card)
    second = heapq.heappop(card)

    result += first + second
    heapq.heappush(card, first + second)


print(result)
