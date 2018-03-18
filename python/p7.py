import sys

from helpers import nth_prime


if __name__ == "__main__":
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = 10001
    print(nth_prime(n))
