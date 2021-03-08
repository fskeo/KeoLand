from math import sqrt


def sum_of_divisors(n):
    total = 0
    for i in range(1, int(sqrt(n) + 1)):
        if n % i == 0 and i != sqrt(n):
            total += i + n // i
        elif i == sqrt(n):
            total += i
    return total - n


def solution(n):
    """Returns the sum of all the amicable numbers under n.

    >>> solution(10000)
    31626
    >>> solution(5000)
    8442
    >>> solution(1000)
    504
    >>> solution(100)
    0
    >>> solution(50)
    0
    """
    total = sum(
        [
            i
            for i in range(1, n)
            if sum_of_divisors(sum_of_divisors(i)) == i and sum_of_divisors(i) != i
        ]
    )
    return total


if __name__ == "__main__":
    print(solution(int(str(input()).strip())))
