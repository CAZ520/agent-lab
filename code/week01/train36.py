def is_even(n):
    return n % 2 == 0


print(is_even(4))
print(is_even(7))


def max_of_three(a, b, c):
    if a >= b and a >= c:
        return a
    if b >= a and b >= c:
        return b
    if c >= b and c >= a:
        return c


print(max_of_three(3, 9, 5))
