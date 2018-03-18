from functools import lru_cache


def next_collatz(n):
    return 3 * n + 1 if n % 2 else n // 2


@lru_cache(maxsize=None)
def collatz(n):
    if n == 1:
        return 1
    return 1 + collatz(next_collatz(n))


if __name__ == "__main__":
    best = 1
    best_i = 1
    for i in range(2, 1000000):
        c = collatz(i)
        if c > best:
            best = c
            best_i = i
    print(best_i)
