# 이것이 코딩 테스트다 - 모험가 길드 (그리디)

users = [2,3,1,2,2]

users.sort()
result = 0
group = []
for user in users:
    if not group :
        group.append(user)
    else:
        if len(group) ==max(group):
            result +=1
            group = [user]
        else:
            group.append(user)
    print(group)
print(result)

    