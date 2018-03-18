def is_palindrome(x):
    tmp = x
    rev = 0
    while tmp > 0:
        rev = 10 * rev + tmp % 10
        tmp //= 10
    return x == rev


if __name__ == "__main__":
    i, j = 999, 999
    best = 0

    while True:
        if is_palindrome(i * j):
            best = max(best, i * j)
            i -= 1
            j = 999
            if (i * j < best):
                # it may be possible to do better by decreasing i and setting j
                # to 999, but if i * j is already smaller than the best answer
                # we have, we can end the search.
                break
        else:
            j -= 1

    print(best)
