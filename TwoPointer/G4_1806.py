n,s = map(int, input().split())
nums = list(map(int, input().split()))
st, en = 0,0
MIN = 100001
tot = nums[st]
for st in range(n):
    while tot < s and en < n:
        en +=1
        if en < n : tot += nums[en]
    if en == n: break
    MIN = min(MIN, en-st +1)
    tot -= nums[st]
if MIN ==100001 : MIN = 0
print(MIN)