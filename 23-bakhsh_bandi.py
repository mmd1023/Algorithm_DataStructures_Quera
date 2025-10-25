n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(arr[0])
    exit()


toutal_sum = sum(arr)
ans = float('inf')

for mask1 in range(1, (1<<n)-1):
    sum = 0
    for i in range(n):
        if mask1 & (1<<i):
            sum += arr[i]

    ans = min(ans, abs(toutal_sum - 2 * sum))

print(ans)


# n = int(input())
# arr = list(map(int, input().split()))

# if n == 1:
#     print(arr[0])
#     exit()

# ans = float('inf')

# for mask1 in range(1, (1<<n)-1):
#     mask2 = (1<<n) - 1 - mask1

#     sum1, sum2 = 0, 0
#     for i in range(n):
#         sum1 += arr[i] if mask1 & (1<<i) else 0
#         sum2 += arr[i] if mask2 & (1<<i) else 0

#     ans = min(ans, abs(sum2 - sum1))

# print(ans)
