n = int(input())
for _ in range(n):
    p = int(input())
    d = dict()
    for _ in range(p):
        c, name = input().split()
        d[int(c)]=name
    print(d.get(max(d.keys())))
