j=0
while True:
    str = input()
    if str[0]=='-': break
    cnt =0
    stk = []
    for s in str:
        if s =='{':
            stk.append(s)
        else:
            if(not stk):
                cnt +=1
                stk.append(s)
            else: stk.pop()
    ccnt=0
    while stk:
        ccnt+=1
        stk.pop()
    j+=1
    cnt = cnt + ccnt//2
    print(f"{j}. {cnt}")