# 이것이 코딩테스트다 - 시각(구현)

#15 - 1분
#10분 - 135 + 60 = 195
#1시간  = 1575 

n = 5
result = 0 
if n>=3 :
    result +=3600
result += (n) * 1575

print( result)

'''
h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in  range(60):
            if '3' in str(i)+str(j)+str(k):
                count +=1
print(count)   
'''
    