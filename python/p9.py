import sys
from math import sqrt


def find_triple(n):
    for i in range(1, n // 3 + 1):
        for j in range(i, n + 1 - 2 * i):
            c = sqrt(i**2 + j**2)
            if i + j + c == 1000:
                return i * j * int(c)


if __name__ == "__main__":
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = 1000
    print(find_triple(n))
