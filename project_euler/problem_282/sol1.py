"""
Project Euler Problem 282:
https://projecteuler.net/problem=282

For non-negative integers m, n the Ackermann function A(m, n) is defined as follows:
          [  n + 1               if m = 0
A(m, n) = [  A(m-1, 1)           if m > 0 and n = 0
          [  A(m-1, A(m, n-1))   if m > 0 and n > 0

For example A(1, 0) = 2, A(2, 2) = 7 and A(3, 4) = 125

Find the sum of A(n, n) with 0 <= n <= 6 and give the answer mod 14^8
"""

from functools import lru_cache

# import sys

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(3000)


# A = [[None]]
# # global A
#
# def save_result(m, n, result):
#     global A
#     while len(A) <= m:
#         A.append([None])
#     while len(A[m]) <= n:
#         A[m].append([None])
#     A[m][n] = result
#
# def read_result(m, n):
#     # print(m, n, A)
#     if len(A) > m:
#         if len(A[m]) > n:
#             return A[m][n]


@lru_cache(None)
def ackermann(m: int, n: int):
    """
    >>> ackermann(1, 0)
    2

    >>> ackermann(2, 2)
    7

    >>> ackermann(3, 4)
    125
    """
    # old_result = read_result(m, n)
    # if old_result:
    #     return old_result
    # if m == 0:
    #     return n + 1
    # elif m > 0 and n == 0:
    #     return ackermann(m - 1, 1)
    # else:
    #     return ackermann(m - 1, ackermann(m, n - 1))


    return (n + 1) if m == 0 else (
        (n + 2) if m == 1 else (
            (2 * n + 3) if m == 2 else (
                (8 * (2 ** n - 1) + 5) if m == 3 else (
                    ackermann(m - 1, 1) if n == 0 else ackermann(m - 1, ackermann(m, n - 1))))))
# save_result(m, n, result)
    # return result


def solution():
    s = 0
    for i in range(0, 7):
        print(i)
        s += ackermann(i, i)
    return s % 14 ** 8


if __name__ == "__main__":
    # for i in range(1, 7):
    # i = 4
    # print(ackermann(i, i), flush=True)
    # print(A)
    print(solution())
