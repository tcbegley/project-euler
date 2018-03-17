import sys


def get_even_sum(n):
    cur = 2
    prev = 1
    total = 0

    # we know that even terms are every third term, and
    # a_{3n+2} = a_{3n+1} + a_{3n} = 2 * a_{3n} + a_{3n-1}
    # a_{3n+3} = a_{3n+2} + a_{3n+1} = 3 * a_{3n} + 2 * a_{3n-1}
    while cur <= n:
        total += cur
        cur, prev = 3 * cur + 2 * prev, 2 * cur + prev

    return total


if __name__ == "__main__":
    if len(sys.argv) == 2:
        limit = int(sys.argv[1])
    else:
        limit = 4000000
    print(get_even_sum(limit))
