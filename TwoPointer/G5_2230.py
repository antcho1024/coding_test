n,m = map(int,input().split())
list =[]
for _ in range(n):
    tmp = int(input())
    list.append(tmp)
list.sort()

st=0
en=0
MIN=2000000001
while True:
    if en >n-1 or st> n-1 : break
    if list[en]- list[st] >=m:
        MIN = min(MIN, list[en]- list[st])
        st+=1
    else :
        en += 1
print(MIN)