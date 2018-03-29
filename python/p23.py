from helpers import sum_factors


def is_abundant(x):
    # sum_factors sums all factors, not just proper factors
    # hence we compare to 2 * x rather than x
    return sum_factors(x) > 2 * x


if __name__ == "__main__":
    abundant = [i for i in range(12, 28111) if is_abundant(i)]
    is_abundant_sum = [False] * (max(abundant) * 2 + 1)
    for i in abundant:
        for j in abundant:
            if j > i:
                break
            is_abundant_sum[i + j] = True
    total = 0
    for i in range(28123):
        if not is_abundant_sum[i]:
            total += i
    print(total)
