n = int(input())
nums = map(int, input().split())
cnt = 0
for x in nums:
    tmp=0
    if(x == 1) : continue
    for i in range(2,x//2+1):
        if(x%i==0) :
            tmp = 1
            break
    if(tmp==0): cnt+=1
print(cnt)