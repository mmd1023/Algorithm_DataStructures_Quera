MOD = 10**9 + 7

n, x = map(int, input().split())
arr = list(map(int, input().split()))

x %= MOD

result = 0
for a in arr:
    result = (result * x + a) % MOD

print(result)
