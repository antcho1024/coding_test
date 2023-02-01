m= int(input())
n= int(input())
sum = 0
tmp = -1
for i in range(m,n+1):
    j=1
    while j*j<i+1 :
        if j*j == i :
            if sum ==0 :
                tmp = i
            sum += i
        j += 1
if tmp != -1:
    print(str(sum))
print(str(tmp))
