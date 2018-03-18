if __name__ == "__main__":
    with open("../data/p67.txt", "r") as f:
        tree = [
            [int(x) for x in row.strip().split(' ')]
            for row in f.read().strip().split('\n')
        ]

    for i in range(len(tree)-2, -1, -1):
        for j in range(len(tree[i])):
            tree[i][j] += max(tree[i+1][j], tree[i+1][j+1])

    print(tree[0][0])
