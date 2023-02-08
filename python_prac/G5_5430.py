from collections import deque
n= int(input())
for _ in range(n):
    error = False
    func = input()
    k = int(input())
    case = deque(input()[1:-1].split(','))
    rev =0
    for c in func:
        if(c=='R'):
            rev +=1
        elif(c=='D'):
            if k==0:
                error=True
                break
            else:
                if rev % 2 == 0:
                    case.popleft()
                else:
                    case.pop()
                k -=1
    if error:print("error")
    else :
        if rev%2!=0 :case.reverse()
        print("[" + ",".join(case) + "]")