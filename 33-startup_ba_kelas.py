A, _, C, __ = map(int, input().split())

# We only take chocolate from A and C, so we can determine the steps based on only these two
steps = 2 * C if A > C else 2 * A - 1

# Initialize the array to store the number of chocolates each participant eats
ans = [steps // 4] * 4

# Distribute the remaining chocolates to the participants
for i in range(steps % 4):
    ans[i] += 1

print(*ans, sep=' ')



# choco1, _, choco3, _ = map(int, input().split())
# counts = [0] * 4

# flag = 1

# while choco1 > 0 and choco3 > 0:
#     for i in range(4):
#         if choco1 <= 0 or choco3 <= 0:
#             break

#         if flag: choco1 -= 1
#         else: choco3 -= 1

#         counts[i] += 1
#         flag = not flag

# print(*counts, sep=' ')