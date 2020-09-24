#  이것이 코딩 테스트다 - 볼링공 고르기 

import collections

numbers = [1,5,4,3,2,4,5,2]

dic = collections.defaultdict(int)

for number in numbers:
    dic[number] +=1


sorted(dic.items())
result = 0
total_ball = len(numbers)
for key in dic.keys():
    total_ball-= dic[key]
    result += dic[key]*total_ball
print(result)
    