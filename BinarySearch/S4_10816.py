from bisect import bisect_left, bisect_right
def countByRange (list, leftValue, rightValue):
    leftIndex = bisect_left(list,leftValue)
    rightIndex = bisect_right(list,rightValue)
    return rightIndex-leftIndex

n = int(input())
nums = list(map(int, input().split()))
m = int(input())
xs = list(map(int, input().split()))
nums.sort()

for x in xs:
    print(countByRange(nums,x,x), end=' ')