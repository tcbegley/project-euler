def sum_divisors(n):
    total, i = 1, 2
    while i**2 <= n:
        if n % i == 0:
            total += i
            if n != i**2:
                total += n // i
        i += 1
    return total


if __name__ == "__main__":
    amicables = set()
    for a in range(1, 10000):
        b = sum_divisors(a)
        if a == sum_divisors(b) and b != a:
            amicables.add(a)
    print(sum(amicables))
