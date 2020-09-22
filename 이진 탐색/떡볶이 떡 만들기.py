# 이것이 코딩 테스트다 - 떡볶이 떡 만들기(이진 탐색)


wanted = 6
cakes = [10,15,17,19]
# high = max (cakes)19 -1
high = max(cakes) - 1
low = 0


def cut_cake(h: int) -> int:
    length = 0
    for cake in cakes:
        if cake > h:
            length += cake - h
    return length


answer = 0

while (low <= high):
    
    mid = (high + low) // 2

    if wanted > cut_cake(mid):
        high = mid -1
        
    elif wanted < cut_cake(mid):
        low = mid +1
        answer = mid
    else:
        answer = mid
        break

print(answer)
