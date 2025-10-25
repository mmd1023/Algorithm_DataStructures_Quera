n, k, L = map(int, input().split())
pos = list(map(int, input().split()))

current_pos = 0
lssi = 0 # last_selected_station_index
optimum_station = []

if pos[0] - 0 > k or L - pos[-1] > k:
    print(-1)
    exit()

for i in range(1, n):
    if pos[i] - pos[i-1] > k:
        print(-1)
        exit()

    if current_pos + k < pos[i]:
        optimum_station.append(lssi+1)
        current_pos = pos[lssi]

    lssi = i

if current_pos + k < L:
    optimum_station.append(lssi + 1)

print(len(optimum_station))
print(*optimum_station, sep=' ')



# def find_closest_smaller(pos, p):
#     low, high = 0, len(pos) - 1
#     best = (-1, -1)
#     while low <= high:
#         mid = (low + high) // 2
#         if pos[mid] <= p:
#             best = (pos[mid], mid)
#             low = mid + 1
#         else:
#             high = mid - 1
#     return best


# n, k, L = map(int, input().split())
# pos = list(map(int, input().split())) + [L]

# current_pos = pos_i = count = 0
# optimum_station = [] 

# while current_pos < L:
#     current_pos, pos_i = find_closest_smaller(pos, current_pos + k)
#     optimum_station.append(pos_i + 1)
#     if pos_i + 1 < len(pos):
#         if pos[pos_i] + k < pos[pos_i+1]:
#             print(-1)
#             exit()
#     elif pos[pos_i] + k < L:
#         print(-1)
#         exit()
#     count += 1

# print(count-1)
# print(*optimum_station[:-1], sep=' ')