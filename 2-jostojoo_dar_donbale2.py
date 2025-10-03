n, q = map(int, input().split())
arr = list(map(int, input().split()))

max_a = max(arr)

cnt = [0] * (max_a + 1)
dp = [0] * (max_a + 2)

for a in arr:
    cnt[a] += 1

dp[2] = cnt[1]

for i in range(3, max_a + 2):
    dp[i] = dp[i-1] + cnt[i-1]


for _ in range(q):
    x = int(input())
    x = min(x, max_a+1)
    print(dp[x])