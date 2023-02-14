### tot = nums[st] 로 놓는 상황
# n, m = map(int , input().split())
# nums = list(map(int, input().split()))
#
# st, en=0,0
# tot, cnt =nums[st],0
#
# while True:
#     if tot == m:
#         cnt +=1
#     if tot >= m:
#         tot -= nums[st]
#         st+=1
#     if en == n : break
#     if tot < m :
#         en +=1
#         if en < n: tot += nums[en]
# print(cnt)


### tot = 0 로 놓는 상황
n, m = map(int , input().split())
nums = list(map(int, input().split()))

st, en=0,0
tot, cnt =0,0

while True:
    if tot == m:cnt +=1

    if tot >= m:
        tot -= nums[st]
        st+=1
# 여기를 elif 가 아닌 if로 해버리면  en이 마지막 이고 st 를 키워 나가려하는 순간에 걍 끝나버림
# 그래서 m 보다 크진 않은 상황(st를 키워갈 상황은 아님) 일떄 en 키우기 전에 검사
    elif en == n : break
    else :
        tot += nums[en]
        en +=1
print(cnt)