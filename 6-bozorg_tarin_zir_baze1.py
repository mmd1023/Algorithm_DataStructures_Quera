n = int(input())
arr = list(map(int, input().split()))

max_sum = float('-inf')
for i in range(n):
    for j in range(i+1, n+1):
        max_sum = max(max_sum, sum(arr[i:j]))

print(max_sum)