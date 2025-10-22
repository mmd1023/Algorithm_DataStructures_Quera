def bin_generator(n, current):
    if n <= 1:
        return current

    current += current[::-1]

    for i in range(len(current)//2):
        current[i] = '0' + current[i]

    for i in range(len(current)//2, len(current)):
        current[i] = '1' + current[i]
    
    return bin_generator(n-1, current)


n = int(input())
print(*bin_generator(n, ['0', '1']), sep='\n')




# def bin_generator(n, val):
#     if n <= 1:
#         print(val)
#         return

#     bin_generator(n-1, val+'0')
#     bin_generator(n-1, val+'1')


# n = int(input())
# bin_generator(n, '0')
# bin_generator(n, '1')