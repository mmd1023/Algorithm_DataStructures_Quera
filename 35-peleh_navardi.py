n = int(input())

dp = [0] * (n + 1)
dp[0] = 1

for i in range(1, n+1):
    dp[i] += dp[i-1]
    dp[i] += dp[i-2] if i - 2 >= 0 else 0
    dp[i] += dp[i-5] if i - 5 >= 0 else 0

print(dp[n])


# def solve(n):
#     if n == 0:
#         return 1
#     elif n < 0:
#         return 0

#     return solve(n-1) + solve(n-2) + solve(n-5)

# print(solve(n))