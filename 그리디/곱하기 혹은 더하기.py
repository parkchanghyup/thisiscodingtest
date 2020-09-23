# 이것이 코딩 테스트다 - 곱하기 혹은 더하기 (그리디)

nums = '02984'

result  = int(nums[0])
for i in range(1,len(nums)):
    if result + int(nums[i]) > result * int(nums[i]) :
        result +=int(nums[i])
    else :
        result *= int (nums[i])


print(result)
    
    
