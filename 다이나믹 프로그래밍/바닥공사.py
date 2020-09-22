# 이것이 코딩 테스트다 - 바닥 공사 (DP) 
import  collections 
N = 3
dp = collections.defaultdict(int)

dp[1] =1
dp [2] =3
for i in range(3,N+1):
    dp[i] = (dp[i-1] + dp[i-2]*2) % 796796
print(dp[N])
# dp[3]= 5
# dp [4] = 11