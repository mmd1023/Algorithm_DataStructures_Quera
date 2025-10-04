n = int(input())
arr = list(map(int, input().split()))

misplaced = 0
for i in range(n):
    misplaced += 1 if arr[i] != i + 1 else 0

print('YES' if misplaced == 2 else 'NO')