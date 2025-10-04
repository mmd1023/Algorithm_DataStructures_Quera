n = int(input())

count = 0

for a in range(1, n // 2 + 1):
    for b in range(a, n - a):
        c = n - (a + b)
        count += 1 if b <= c and c < a + b else 0

print(count)