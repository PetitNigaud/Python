"""
Project Euler Problem 204: https://projecteuler.net/problem=204

A Hamming number is a positive number which has no prime factor larger than 5.
So the first few Hamming numbers are 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15.
There are 1105 Hamming numbers not exceeding 10^8.
We will call a positive number a generalised Hamming number of type n, if it has no prime factor larger than n.
Hence the Hamming numbers are the generalised Hamming numbers of type 5.
How many generalised Hamming numbers of type 100 are there which don't exceed 10^9?

In the solution...

"""

import time
from itertools import combinations_with_replacement, cycle
from math import prod, log2


def prime_sieve_eratosthenes(num):
    """
    print the prime numbers up to n

    >>> prime_sieve_eratosthenes(10)
    [2, 3, 5, 7]

    >>> prime_sieve_eratosthenes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """

    is_prime = [True for i in range(num + 1)]
    p = 2

    while p * p <= num:
        if is_prime[p]:
            for i in range(p * p, num + 1, p):
                is_prime[i] = False
        p += 1

    primes = []
    for nr in range(2, len(is_prime)):
        if is_prime[nr]:
            primes.append(nr)
    return primes


def solution(limit: int = 10**9, hamming_type: int = 100):
    """

    >>> solution(15, 5)
    11

    >>> solution(10**8, 5)
    1105

    >>> solution(10**9, 5)
    1530

    # >>> solution(10**6, 100)
    # 72271

    >>> solution(10**9, 100)
    2944730

    """

    t0 = time.time()
    prime_factors = prime_sieve_eratosthenes(hamming_type)

    new_values = [1]
    count = 1
    while True:
        last_values, new_values = new_values, []
        for last in last_values:
            for factor in prime_factors:
                prod = last * factor
                if prod <= limit:
                    if prod not in new_values:
                        new_values.append(prod)
                else:
                    break

        if len(new_values) == 0:
            print(count)
            print(f"elapsed time {time.time() - t0} s")
            return count
        else:
            count += len(new_values)




if __name__ == "__main__":
    print(solution())
