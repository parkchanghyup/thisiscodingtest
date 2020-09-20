# 이것이 코딩테스트다 - 숫자 카드 게임 (그리디)

n,m = 2,4
arr = [[7,3,1,8],[3,3,3,4]]
results = []

for i in range(n):
    results.append(min(arr[i]))
print(max(results))
