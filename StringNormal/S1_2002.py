import sys
n = int(input())
st = []
en = []

for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    st.append(tmp)
for _ in range(n):
    tmp = sys.stdin.readline().rstrip()
    en.append(tmp)

k=-1
cnt = 0
for i in range(n):
    index = en.index(st[i])
    if index < k :
        continue
    cnt += index-1-k
    k = index
print(cnt)