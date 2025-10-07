print(5 if (n:=int(input())) == 0 else [-5, 25, 4, 16][n%4])


# out = [-5, 25, 4, 16]
# n = int(input())
# print(5 if n == 0 else out[n%4])


# import sys
# sys.setrecursionlimit(10**6)

# def f(n):
#     if n == 0:
#         return 5
#     return f(n-1) ** 2 if n&1 else f(n-1) - 21

# print(f(n))