
# 여행계획

# 원소가 속한 집합 찾기

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())
parent = [0] * (n + 1)

# 자기자신을 부모노드로
for i in range(1, n + 1):
    parent[i] = i

# union 연산 수행

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1:
            union_parent(parent, i + 1, j + 1)

# 여행 계획 입력받기
plans = list(map(int, input().split()))

result = True
for idx in range(len(plans) - 1):
    if find_parent(parent, plans[idx]) != find_parent(parent, plans[idx + 1]):
        result = False

print(result)

