# 이것이 코딩테스트다 - 큰수의 법칙 (그리디)

# N, M, K를 공백을 기준으로 구분하여 입력 받기
#n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
#data = list(map(int, input().split()))
n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]
data.sort(reverse=True)

result = 0
for _ in range(int(m / k)):

    for _ in range(k):
        result += data[0]

    result += data[1]

print(result)
'''수학적 아이디어로 문제해결 

# N, M, K를 공백을 기준으로 구분하여 입력 받기
n, m, k = map(int, input().split())
# N개의 수를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split()))

data.sort() # 입력 받은 수들 정렬하기
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

#가장 큰수가 더해지는 횟수
count  = int(m/(k+1)) * k
count += m%(k+1)

result = count * first
result += int(m/(k+1))*second

print(result)
'''