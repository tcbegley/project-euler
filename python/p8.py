import sys
from functools import reduce
from math import inf


if __name__ == "__main__":
    with open('../data/p8.txt', 'r') as f:
        arr = list(map(int, f.read().strip()))

    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = 13

    best = -inf

    for i in range(len(arr) - 1):
        best = max(best, reduce(lambda x, y: x * y, arr[i:i+n]))

    print(best)
