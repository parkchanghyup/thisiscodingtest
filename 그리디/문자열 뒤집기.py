# 이것이 코딩 테스트다 - 문자열 뒤집기 (그리디)

nums = input()

result = [nums[0]]
for i in range(1,len(nums)):
    if result[-1] != nums[i]:
        result.append(nums[i])
        
one = result.count('1')
zero = result.count('1')
if one>zero:
    print(zero)
else :print(one)
 