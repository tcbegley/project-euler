from string import ascii_uppercase


def get_names():
    with open('../data/p22.txt', 'r') as f:
        names = f.read()[1:-1]  # lose leading and trailing " marks
    names = names.split('","')
    return sorted(names)


def score(name):
    return sum(map(lambda x: ascii_uppercase.index(x) + 1, name))


if __name__ == "__main__":
    names = get_names()
    print(sum((i+1) * x for i, x in enumerate(map(score, names))))
