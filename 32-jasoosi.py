n = int(input())
org = [input() for _ in range(n)]
q = int(input())
infos = [input() for _ in range(q)]

if q == 0:
    print(0)
    exit()

i = 0
ans = 0
last_chosen = infos[0]
while i < q:
    counter = {infos[i]: 1}
    next_step = i + 1
    for j in range(i + 1, q):
        counter[infos[j]] = 1 if infos[j] not in counter else counter[infos[j]] + 1
        next_step = j

        if len(counter) >= n: break

    i = next_step

    if last_chosen in counter:
        chosen = infos[i] if i < q else last_chosen

        if len(counter) < n:
            for o in org:
                if o not in counter:
                    chosen = o
                    break
        
        if chosen != last_chosen:
            last_chosen = chosen
            ans += 1

print(ans - 1)
