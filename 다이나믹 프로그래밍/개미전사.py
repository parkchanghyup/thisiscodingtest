# 이것이 코딩 테스트다 - 개미전사 (DP)

import collections

N=4 
foods = [1,3,1,5]
dp[0] = 0
dp [1] = 1

for i in range(1,len(foods)):
        dp [i]  = max(dp[i-1], dp[i-2]+foods[i])
print(dp[N-1])