n = int(input())
deadline = sorted(list(map(int, input().split())))

current_time = 0
count = 0
for d in deadline:
    if current_time < d:
        count += 1
        current_time += 1

print(count)