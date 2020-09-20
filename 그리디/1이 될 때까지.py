# 이것이 코딩테스트다 - 1이 될 때까지 (그리디)

n,k = 25,5

count = 0 

while n>1:
    if n % k ==0 :
        n = n/k
    else :n-=1
    
    count +=1
print(count)
