n = int(input())
a = sorted(list(map(int, input().split())))

print(med := a[(n-1) // 2], sum(abs(a[i]-med) for i in range(n)))