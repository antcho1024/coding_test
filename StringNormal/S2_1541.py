str = input()
numGroup = str.split('-')
# - 를 기준으로 그룹을 나눔 (아래 예시)
# 55-50+40
# ['55', '50+40']

tmp=0       # 문자열 -> 정수로 변경할 떄 쓰일 변수
r = 0       # 한 그룹당 계산 한 값 저장할 변수
result= 0   # 총 결과
for i in range(len(numGroup)) :
    for s in numGroup[i]:
        if s =='+':
            r +=tmp
            tmp=0
        else:
            if tmp != 0:
                tmp *=10
            tmp+=int(s)
    r += tmp
    tmp = 0

    if i==0:    # 첫번째 그룹이면 + 해주기
        result +=r
    else:       # 나머지는 다 - 해주기
        result -=r
    r=0
print(result)