import sys


def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6


def square_of_sum(n):
    return n**2 * (n + 1)**2 // 4


if __name__ == "__main__":
    if len(sys.argv) == 2:
        n = int(sys.argv[1])
    else:
        n = 100
    diff = square_of_sum(n) - sum_of_squares(n)
    print(f"The difference for n = {n} is: {diff}")
