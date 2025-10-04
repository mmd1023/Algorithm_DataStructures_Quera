n = int(input())

count = 0

for a in range(1, n + 1):
    for b in range(a, n + 1):
        for c in range(b, n + 1):
            count += 1 if a + b + c == n and c < a + b else 0

print(count)