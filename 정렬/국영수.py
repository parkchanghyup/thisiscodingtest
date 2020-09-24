# 이것이 코딩 테스트다 - 국영수 (정렬)
import sys

N = int(input())

student = []

for _ in range(N):
    name, kor, eng, math = input().split()
    student.append([name, int(kor), int(eng), int(math)])

student.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for name, _, _, _ in student:
    print(name)