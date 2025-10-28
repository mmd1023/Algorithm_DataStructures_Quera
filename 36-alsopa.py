from functools import lru_cache

x = int(input())
n = int(input())
max_base = int(x ** (1 / n))

@lru_cache(None)
def count_ways(x, n, base):
    if x == 0:
        return 1
    if x < 0 or base > max_base:
        return 0
    return count_ways(x-(base ** n), n, base + 1) + count_ways(x, n, base + 1) 

print(count_ways(x, n, 1))



# #  bit mask idea
# max_base = int(x ** (1 / n))
# count = 0
# for mask in range(2 ** max_base):
#     sum = 0
#     for i in range(1, max_base + 1):
#         sum += ((mask>>(i-1)) & 1) * i ** n

#     if sum == x:
#         count += 1

# print(count)