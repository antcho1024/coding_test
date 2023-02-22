S = list(input())
T = list(input())
result = 0
while T:
    if T[-1]=='A':
        T.pop()
    else :
        T.pop()
        T.reverse()
    if T == S:
        result = 1
        break
print(result)