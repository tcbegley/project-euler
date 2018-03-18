import sys

from helpers import prime_sieve


if __name__ == "__main__":
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = 2000000
    print(sum(prime_sieve(n)))
