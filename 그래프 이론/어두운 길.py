# 어두운길

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


N, M = map(int, input().split())
parent = [0] * (N+1)

for i in range(1, N+1):
    parent[i] = i
nodes = []

for _ in range(M):
    u, v, w = map(int, input().split())
    nodes.append([u, v, w])

nodes.sort(key=lambda x: x[2])
result  = 0

total_money = 0
for node in nodes:

    u,v,w = node
    total_money +=w

    if find_parent(parent,u) != find_parent(parent,v):
        union_parent(parent,u,v)
        result +=w

print(total_money - result)