from helpers import prime_factorise


def triangle(n):
    return n * (n+1) // 2


def count_factors(n):
    prime_factors = prime_factorise(n)
    primeset = list(set(prime_factors))

    product = 1
    for p in primeset:
        product *= prime_factors.count(p) + 1

    return product


if __name__ == "__main__":
    n = 1
    while count_factors(triangle(n)) < 500:
        n += 1
    print(triangle(n))
