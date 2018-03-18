from helpers import choose


if __name__ == "__main__":
    # a valid route takes 20 right moves, and 20 down moves
    # there are 40C20 ways of ordering this, hence 40C20 distinct routes
    print(choose(40, 20))
