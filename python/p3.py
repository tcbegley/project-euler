import sys

from helpers import prime_factorise

if __name__ == "__main__":
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = 600851475143
    print(prime_factorise(n)[-1])
