# 이것이 코딩테스트다 -왕실의 나이트 (구현)
position = 'a1'
row = int(position[1])
col = ord(position[0]) - ord('a')+ 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2),
         (-2, 1)]
count = 0


for step in steps:
    new_row = row +step[0]
    new_col = col + step[1]
        
    if new_row <1 or new_row >8 :
        continue
    elif new_col <1 or new_col >8 :
        continue

    count +=1
    
print(count)
        
    