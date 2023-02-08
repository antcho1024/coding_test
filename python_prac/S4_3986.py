import sys
n= int(input())
cnt=0
for _ in range(n):
    str= sys.stdin.readline().rstrip()
    stk=[]
    for s in str:
        if stk and s == stk[-1]:
            stk.pop()
        else:
            stk.append(s)

    if not stk:
        cnt += 1
print(cnt)

