from bisect import bisect_left, bisect_right

def binary_search1(target, start, end, data):
    if start > end:
        return None
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return binary_search1(target, start, mid-1, data)
    else:
        return binary_search1(target, mid+1, end, data)


def binary_search2(target, start, end, data):
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

#'정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때 사용
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index