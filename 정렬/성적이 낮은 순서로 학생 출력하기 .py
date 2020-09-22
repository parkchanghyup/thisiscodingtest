# 이것이 코딩 테스트다 - 성적이 낮은 순서로 학생 출력하기 ( 정렬 )

name = [('홍길동',95),('이순신',100),('장영실',98)]

name.sort(key =lambda x : x[1],reverse=True)
for _ in name:
    print(_[0],end=' ')
