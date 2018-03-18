"""
Helper functions for Python solutions
"""


def prime_sieve(limit):
    """
    Generate all primes less than limit.
    """
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for j in range(i*i, limit, i):
                a[j] = False


def factor(x):
    """
    Find smallest non-trivial factor of x. Returns 0 if none found, and so can
    be used as a primality test.
    """
    if x % 2 == 0:
        return 2
    else:
        i = 3
        while i * i <= x:
            if x % i == 0:
                return i
            else:
                i += 2
        return 0


def prime_factorise(x):
    """
    Find the prime factorisation of x.
    """
    factors = []
    f = factor(x)
    while f:
        while x % f == 0:
            factors.append(f)
            x //= f
        f = factor(x)
    if x != 1:
        factors.append(x)
    return factors
