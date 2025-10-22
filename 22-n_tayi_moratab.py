def generate(n, step, current_comb):
    if step <= 0:
        print(current_comb); return
    
    for i in range(1, n+1):
        generate(n, step-1, current_comb + str(i) + ' ')


n = int(input())
generate(n, n, '')