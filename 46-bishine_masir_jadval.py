# 100% with pypy3
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

dp = [[0]*m for _ in range(n)]
dp_direction = [['']*m for _ in range(n)]
dp[n-1][0] = matrix[n-1][0]

# iterate anti-diagonal: j - i = d
for d in range(-n + 2, m):
    for i in range(n):
        j = i + d
        if 0 <= j < m:
            left = dp[i][j-1] if j-1 >= 0 else float('-inf')
            down = dp[i+1][j] if i+1 < n else float('-inf')
            
            dp_direction[i][j] = "R" if left > down else "U"
            dp[i][j] = matrix[i][j] + max(left, down)

# Reconstruct path
path = ""
i, j = 0, m - 1
while not (i == n - 1 and j == 0):
    dir = dp_direction[i][j]
    path += dir
    if dir == "R":
        j -= 1
    else:
        i += 1

print(dp[0][m-1])
print(path[::-1])



# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]

# max_sum = float('-inf')
# best_path = ""

# def solve(i, j, path_sum, current_path):
#     global max_sum, best_path
#     if i == 0 and j == m - 1:
#         if max_sum < path_sum:
#             max_sum = path_sum
#             best_path = current_path
#         return
    
#     if j < m - 1:
#         solve(i, j+1, path_sum+matrix[i][j+1], current_path+"R")
#     if i > 0:
#         solve(i-1, j, path_sum+matrix[i-1][j], current_path+"U")

# solve(n-1, 0, matrix[n-1][0], "")

# print(max_sum)
# print(best_path)