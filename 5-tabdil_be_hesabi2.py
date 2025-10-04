n, k = map(int, input().split())

# a[i] = x + i * k
a = list(map(int, input().split()))

# b[i] = a[i] - i * k -----> x
b = [a[i] - i * k for i in range(n)]

# optimum x = median 
median = sorted(b)[n // 2]

cost = 0
for i in range(n):
    cost += abs(median - b[i])

print(cost)