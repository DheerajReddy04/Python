def binary_search(arr, key):
    low = 0
    high = 1
    while high < len(arr) and arr[high] <key:
        low = high
        high = high * 2

    while low <= high and low <len(arr):
        mid = low + (high-low) // 2
        try:
            if arr[mid] == key:
                return mid
            if arr[mid] < key:
                low = mid + 1
            else:
                high = mid -1
        except IndexError:
            high = mid -1
    return -1
key = int(input())
arr = list(map(int, input().split()))
result = binary_search(arr, key)
if result != -1:
    print(result)
else:
    print("-1")