import math
def isDecimal (n):
    if n < 2: return False
    for i in range(2,int(math.sqrt(n)+1)):
        if n%i==0: return False
    return True

while True:
    str = input()
    if str == '0': break
    MAX = 0

    for i in range(len(str)):
        tmp = int(str[i])
        if isDecimal(tmp) : MAX = max(MAX, tmp)
        for j in range(i+1,len(str)):
            if j > i+4 : break
            tmp *=10
            tmp += int(str[j])
            if isDecimal(tmp): MAX = max(MAX, tmp)
    print(MAX)

### 위에는 수 하나하나가 소수인지 판별
### 아래는 에라토스테네스 체 를 사용해서 소수를 100000 아래까지 다 리스트에 넣어놓고
### 그 수들이 str에 있는지 확인
# def prime(n):
#     li = [1]*(n+1)
#     for i in range(2, int(n**0.5)+1):
#         if li[i]:
#             for j in range(i+i, n+1, i):
#                 li[j] = 0
#     p = [i for i in range(2, n+1) if li[i]]
#     return p
#
# while 1:
#     s = input()
#     if s == '0':
#         break
#     p = prime(100000)
#     res = 2
#     for n in p:
#         if str(n) in s:
#             res = n
#     print(res)