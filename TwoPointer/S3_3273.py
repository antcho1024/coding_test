# from itertools import combinations
# n = int(input())
# nums = map(int, input().split())
# x = int(input())
#
# coms = list(combinations(nums,2))
# cnt=0
# for com in coms:
#     if com[0]+com[1]==x :cnt+=1
# print(cnt)

###### 위의 경우 메모리 초과 ######

# n = int(input())
# nums = list(map(int, input().split()))
# x = int(input())
#
# nums.sort()
# cnt=0
# i=0
# while i<n:
#     if nums[i]>x : break
#     j = i+1
#     while j<n:
#         if nums[j] > x: break
#         if nums[i]+nums[j]==x : cnt+=1
#         elif nums[i]+nums[j] > x : break
#         j+=1
#     i+=1
# print(cnt)


###### 위의 경우 시간 초과 ######

###### 투포인터 방법 사용 ######
n = int(input())
nums = list(map(int, input().split()))
x = int(input())

nums.sort()
st,en =0, n-1
cnt=0
while st!=en:
    sum = nums[st] + nums[en]
    if sum == x: cnt +=1
    if sum <= x:
        st+=1
    else:
        en -=1
    if en <0 or st > n-1: break
print(cnt)