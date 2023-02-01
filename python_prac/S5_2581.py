import math
def isDecimal(x):
    if x == 1: return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

m = int(input())
n= int(input())
min = -1
sum=0
for i in range(m,n+1):
    if(isDecimal(i)) :
        sum += i
        if(min==-1) :
            min = i
if(min!=-1):
    print(sum)
print(min)