import math
n = int(input())

p = math.factorial(n)
cnt=0
while 1:
    if p%10 == 0 : cnt +=1
    else : break
    p=p//10

print(cnt)