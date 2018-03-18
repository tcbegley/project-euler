def zeller(d, m, y):
    """
    Compute day of week given day, month, year as input.

    https://en.wikipedia.org/wiki/Zeller%27s_congruence
    """
    y2 = y % 100
    century = y // 100
    w = d + (13 * (m + 1)) // 5 + y2 + y2 // 4 + century // 4 - 2 * century
    return w % 7


if __name__ == "__main__":
    count = 0
    for i in range(1901, 2001):
        for j in range(3, 15):
            # months are encoded 3,...,14 in the algorithm
            if zeller(1, j, i) == 1:
                count += 1
    print(count)
