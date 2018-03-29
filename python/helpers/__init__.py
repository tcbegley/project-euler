"""
Helper functions for Python solutions
"""
from math import log


def nth_prime(n):
    """
    Find nth prime
    """
    lim = 14
    if n >= 6:
        # if n >= 6, an upper bound on nth prime is n(log(n) + log(log(n)))
        lim = int(n * (log(n) + log(log(n))))
    a = [True] * lim
    count = 0
    for i in range(2, lim):
        if a[i]:
            count += 1
            if count == n:
                return i
            for j in range(i*i, lim, i):
                a[j] = False


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


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def choose(n, k):
    """
    A fast way to compute binomial coefficients by Andrew Dalke.
    """
    if 0 <= k <= n:
        num = 1
        den = 1
        for i in range(1, min(k, n - k) + 1):
            num *= n
            den *= i
            n -= 1
        return num // den
    else:
        return 0


def sum_factors(n):
    prod = 1
    k = 2
    while k*k <= n:
        p = 1
        while n % k == 0:
            p = p * k + 1
            n //= k
        prod *= p
        k += 1
    if n > 1:
        # if n is greater than 1, then there is one unaccounted for prime
        # factor
        prod *= 1 + n
    return prod
