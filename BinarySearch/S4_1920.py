def binarySearch (list, target, start, end):
    if start > end :return None
    mid = (end + start)//2
    if list[mid] == target : return mid
    elif list[mid] < target : return binarySearch(list, target, mid+1, end)
    elif list[mid] > target : return binarySearch(list, target, start, mid-1)


n = int(input())
nums = list(map(int, input().split()))
m = int(input())
xs = list(map(int, input().split()))
nums.sort()

for x in xs :
    if binarySearch(nums,x,0,n-1) is not None : print("1")
    else : print("0")