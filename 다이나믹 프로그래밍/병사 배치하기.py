# 병사 배치하기 (dP)

n = int(input())
array = list(map(int,input().split()))
# 순서를 뒤집어 ' 가장 긴 증가하는 부분수열' 문제로 변환

dp = [0] * n

for i in range(n):
    for j in range(i):
        if array[j] < array[i] :
            dp[i] = max(dp[i] , dp[j] + 1)
print(dp)
    