# 이것이 코딩테스트다 - 팀 결성 (그래프 이론)
from typing import List


def find_parent(parent:List, x:int):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]


def union_parent(parent: List, a: int, b: int):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i

result = []
for _ in range(m):
    func, a, b = map(int, input().split())
    if func == 0:
        union_parent(parent,a,b)
    else :
        if find_parent(parent,a) != find_parent(parent,b):
            result.append('NO')
        else :
            result.append('YES')

print(result)


'''
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
['NO', 'NO', 'YES']

'''