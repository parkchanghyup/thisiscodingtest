# 크루스칼

# 특정 노드가 속한 원소 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


# 두 원소가 속한 집합  합치기

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 개수와 간선의 개수 입력 받기

v, e = map(int, input().split())
parent = [0] * (v + 1)  # 부모 테이블 초기화

# 부모 테이블 상에서 ,부모를 자기 자신으로 초기화
for i in range(1,v + 1):
    parent[i] = i

nodes = []
for i in range(e):
    a, b, weight = map(int, input().split())
    nodes.append([a, b, weight])

nodes.sort(key=lambda x: x[2])

result = 0
for node in nodes:
    print(node,find_parent(parent,node[0]) ,find_parent(parent,node[1]))
    if find_parent(parent,node[0]) != find_parent(parent,node[1]):

        union_parent(parent, node[0], node[1])
        result += node[2]

print(result)

