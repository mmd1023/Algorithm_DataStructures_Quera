n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

prefix_sum = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        prefix_sum[i][j] = matrix[i][j] + (prefix_sum[i-1][j] if i > 0 else 0)


def kadane(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


total_max = float("-inf")

for i in range(n):
    for j in range(i, n):
        columns_sum = [0] * m
        for c in range(m):
            columns_sum[c] = prefix_sum[j][c] - (prefix_sum[i-1][c] if i > 0 else 0)
        total_max = max(total_max, kadane(columns_sum))

print(total_max)
