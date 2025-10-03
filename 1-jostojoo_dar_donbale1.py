n, q = map(int, input().split())
arr = sorted(list(map(int, input().split())))

def find_min_place_index(x, arr):
    low, high = 0, len(arr) - 1

    if x <= arr[low]: return low
    if x > arr[high]: return high + 1
    
    while low < high:
        mid = (low + high) // 2

        if arr[mid] < x <= arr[mid+1]: 
            return mid + 1

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] >= x:
            high = mid - 1

    return low + 1

for _ in range(q):
    x = int(input())
    print(find_min_place_index(x, arr))


# for _ in range(q):
#     x = int(input())
#     ans = 0
#     for a in arr:
#         ans += 1 if a < x else 0
#     print(ans)