if __name__ == "__main__":
    with open("../data/p14.txt", "r") as f:
        nums = map(int, f.read().strip().split('\n'))
    print(str(sum(nums))[:10])
