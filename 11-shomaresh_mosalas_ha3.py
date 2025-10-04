n = int(input())
total_count = 0

for a in range(1, n // 3 + 1):
    # p = b + c
    p = n - a

    # x = c - b  -->  c= b + x  -->  p = 2b + x  --> b = (p - x) / 2
    # Triangle condition: c < a + b  -->  b + x < b + a  -->  x < a  --> x <= a - 1
    # Uniqueness condition: a <= b <= c  -->  a <= b , b = (p - x) / 2 -->  2a <= p - x  -->  x < p - 2a , p = b + c  -->  x < a + b + c - 3a  -->  x < n - 3a
    # x upper and lower bound
    upper_bound, lower_bound = min(n - 3 * a, a - 1), 0

    # valid_x = {x ∈ Z , x ∈ [upper_bound, lower_bound]  |  x % 2 == p % 2}
    lower_bound += 1 if p % 2 != lower_bound % 2 else 0
    upper_bound -= 1 if p % 2 != upper_bound % 2 else 0

    # count = (last_x - first_x) / d + 1
    x_count = (upper_bound - lower_bound) // 2 + 1

    total_count += x_count

print(total_count)