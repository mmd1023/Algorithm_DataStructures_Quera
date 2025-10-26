n, V = map(int, input().split())
juice = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0] / x[1], reverse=True)

happyness = 0

for h, v in juice:
    if v < V:
        happyness += h
        V -= v
    else:
        happyness += (V / v) * h
        break

print(happyness)
