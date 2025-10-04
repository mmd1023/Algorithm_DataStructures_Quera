n = int(input())
arr = list(map(int, input().split()))

prefix_sum = [0]
for a in arr: 
    prefix_sum.append(prefix_sum[-1] + a)

max_sum = float('-inf')

for i in range(n):
    for j in range(i+1, n+1):
        max_sum = max(max_sum, prefix_sum[j] - prefix_sum[i])

print(max_sum)