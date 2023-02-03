n = int(input())
for _ in range(n):
    x = int(input())
    list = []
    for i in range(2,x+1):
        cnt=0
        if x%i==0 :
            while x%i==0:
                x = x/i
                cnt+=1
            print(f"{i} {cnt}")