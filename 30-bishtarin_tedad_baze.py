n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[1])

count = 1
last_end = arr[0][1]

for start, end in arr[1:]:
    if last_end <= start:
        count += 1
        last_end = end

print(count)