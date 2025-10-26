n, k = map(int, input().split())
arr = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: x[0])

max_energy = k
for b, a in arr:
    max_energy += a - b if b <= max_energy and b <= a else 0

print(max_energy)