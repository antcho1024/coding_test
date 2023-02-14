### 다시 풀어보기 ###
n = int(input())
### 그냥 소수 구하기 : 시간초과 남
# import math
# def isDecimal(x):
#     if x == 1 : return False
#     for i in range(2,int(math.sqrt(x))+1):
#         if x % i ==0 : return False
#     return True
# def makeDecimalList(x):
#     list=[]
#     for i in range(2,x+1):
#         if isDecimal(i):
#             list.append(i)
#     return list

### 에라토스테네스의 체 : 범위 내 모든 소수 구할 때 효율적
a = [False, False] + [True]*(n-1)
list = []

for i in range(2, n+1):
    if a[i]:
        list.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False

st, en =0,0
tot = 0
cnt =0

while True:
    if tot == n: cnt +=1

    if tot >= n : # = 들어가도 안들어가도 맞음
        tot -= list[st]
        st+=1
    elif en == len(list): break
    else:
        tot += list[en]
        en +=1
print(cnt)