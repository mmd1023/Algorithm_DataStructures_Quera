def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr

n = int(input())
arr = list(map(int, input().split()))

print(*selection_sort(arr))
