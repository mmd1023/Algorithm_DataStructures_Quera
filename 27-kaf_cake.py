n, k = map(int, input().split())
arr = list(map(int, input().split()))

if k >= 3:
    print(min(arr))
elif k == 1:
    print(max(arr))
elif k == 2:
    min_badness = float('inf')
    for seperator in range(1, n):
        min_badness = min(min_badness, max(arr[:seperator]), max(arr[seperator:]))
    print(min_badness)