n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[i][j] = matrix[i][j]
            continue
        left = dp[i][j-1] if j > 0 else float('inf')
        up = dp[i-1][j] if i > 0 else float('inf')
        dp[i][j] = min(left, up) + matrix[i][j]
    
    for j in range(m):
        right = dp[i][(m-j-1)+1] if j > 0 else float('inf')
        dp[i][m-j-1] = min(right + matrix[i][m-j-1], dp[i][m-j-1])

print(dp[n-1][m-1])