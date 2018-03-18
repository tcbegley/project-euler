def count(n, lookup):
    total = 0
    if n // 10 == 0:
        return lookup[n]
    else:
        if (n // 10) % 10 == 1:
            total += lookup[n % 100]
        else:
            total += lookup[(n % 100) - (n % 10)] + lookup[n % 10]
        if n // 100:
            if (n // 100) % 10:
                total += lookup[100] + lookup[(n // 100) % 10]
            if n % 100:
                total += 3  # include 'and' in total characters
        if n // 1000:
            total += lookup[1000] + lookup[n // 1000]
    return total


if __name__ == "__main__":
    with open("../data/p17.txt", "r") as f:
        lines = f.read().strip().split('\n')
    lookup = {}
    for line in lines:
        k, v = map(int, line.split(' '))
        lookup[k] = v
    total = 0
    for i in range(1000):
        total += count(i + 1, lookup)
    print(total)
