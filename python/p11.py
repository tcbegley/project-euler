from functools import reduce
from math import inf


def max_product(grid, n=4):
    rows = len(grid)
    cols = len(grid[0])
    best = -inf

    for i in range(rows + 1 - n):
        for j in range(cols):
            best = max(
                best,
                reduce(
                    lambda x, y: x * y,
                    [grid[k][j] for k in range(i, i + n)]
                )
            )
    for i in range(rows):
        for j in range(cols + 1 - n):
            best = max(
                best,
                reduce(
                    lambda x, y: x * y,
                    [grid[i][k] for k in range(j, j + n)]
                )
            )
    for i in range(rows + 1 - n):
        for j in range(cols + 1 - n):
            best = max(
                best,
                reduce(
                    lambda x, y: x * y,
                    [grid[i + k][j + k] for k in range(n)]
                ),
                reduce(
                    lambda x, y: x * y,
                    [grid[i + k][j + n - 1 - k] for k in range(n)]
                )
            )
    return best


if __name__ == "__main__":
    with open("../data/p11.txt", "r") as f:
        grid = [
            [int(i) for i in x.split(' ')]
            for x in f.read().strip().split('\n')
        ]
    print(max_product(grid))
