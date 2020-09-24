#이것이 코딩 테스트다 - 연산자 끼워넣기 (dfs/bfs)
import sys

N = int(input())

number = list(map(int,sys.stdin.readline().split()))
plus,minus,mul,div = list(map(int,sys.stdin.readline().split()))



max_num = -1e9
min_num = 1e9


def func(idx,num):
    global min_num,max_num,plus,minus,mul,div

    # 종료부
    if idx == N:

        min_num = min(min_num,num)
        max_num = max(max_num,num)
    else :

        if plus > 0:
            plus -=1
            func(idx+1,num+number[idx])
            plus +=1
        if minus > 0:
            minus -=1
            func(idx+1,num-number[idx])
            minus +=1
        if mul > 0:
            mul -=1
            func(idx+1,num*number[idx])
            mul+=1
        if div > 0:
            div -=1
            func(idx+1,int(num/number[idx]))
            div+=1

func(1,number[0])
print(max_num)
print(min_num)

