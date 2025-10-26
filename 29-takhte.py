n, c = map(int, input().split())
arr = sorted(list(map(int, input().split())), reverse=True)

for a in arr:
    d = min(c, max(0, a - c))
    c -= d
    if d == 0:
        break

print(c)