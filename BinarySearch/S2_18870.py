from bisect import bisect_left

n = int(input())
nums = list(map(int, input().split()))

tmp = nums.copy()
tmp = list(set(tmp))
tmp.sort()

for num in nums:
    index = bisect_left(tmp,num)
    print(index,end=" ")

