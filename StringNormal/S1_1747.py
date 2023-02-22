# def makeDecimalList(x,n):
#     a = [False, False] + [True]*(n-1)
#     list=[]
#     for i in range(2,n+1):
#         if a[i]:
#             if i>x-1: list.append(i)
#             for j in range(2*i,n+1,i):
#                 a[j] = False
#     return list
#
# def isPellindrome (n):
#     li = list(str(n))
#     st, en = 0, len(li) - 1
#     while st < en:
#         if li[st] != li[en]: return False
#         st += 1
#         en -= 1
#     return True
# n = int(input())
# decimalList = makeDecimalList(n,10000000)
# for i in decimalList:
#     if isPellindrome(i):
#         print(i)
#         break
#

import math
def isDecimalList(n):
    if n<2 : return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0 : return False
    return True

def isPellindrome (n):
    li = list(str(n))
    st, en = 0, len(li) - 1
    while st < en:
        if li[st] != li[en]: return False
        st += 1
        en -= 1
    return True
n = int(input())
while True:
    if isDecimalList(n):
        if isPellindrome(n):
            print(n)
            break
    n+=1

#둘 다 정답
# 위에꺼 메모리 187508 시간 2636
# 아래꺼 메모리 33376  시간 3392