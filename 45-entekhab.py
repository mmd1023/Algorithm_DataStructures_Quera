MOD = 10 ** 9 + 7

q = int(input())
ns = [0] * q
rs = [0] * q

for i in range(q):
    ns[i], rs[i] = map(int, input().split())

MAX_N = max(ns)

dp = [[0] * (MAX_N+1) for _ in range(MAX_N+1)]
dp[0][0] = 1

for n in range(1, MAX_N+1):
    for r in range(MAX_N+1):
        dp[n][r] = (dp[n-1][r] + (dp[n-1][r-1] if r - 1 >= 0 else 0)) % MOD


for i in range(q):
    print(0 if ns[i] < rs[i] else dp[ns[i]][rs[i]])