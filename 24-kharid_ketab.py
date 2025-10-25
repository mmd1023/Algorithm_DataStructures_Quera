n, r = map(int, input().split())
cost = sorted(list(map(int, input().split())))

count = 0
i = 0
while i < n and r - cost[i] > 0:
    r -= cost[i]
    count += 1
    i += 1

print(count)