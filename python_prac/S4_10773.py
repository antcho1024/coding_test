n = int(input())
stack =[]
sum=0
for _ in range(n):
    k = int(input())
    if(k==0):
        sum -= stack.pop()
    else :
        stack.append(k)
        sum += k
print(sum)