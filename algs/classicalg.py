#!../venv/Scripts/python.exe
# -*- encoding : utf-8 -*-

"""
@Description:  classical.py provides classical algorithm required to reduce factoring problem to period finding problem
@Author: Quentin Delamea
@Copyright: Copyright 2020, PyShor

@License: MIT
@Version: 0.0.1
@Maintainer: nobody

@Status: Stopped
"""

# Standard lib imports
import random as rd

# External libs imports
import numpy as np


def is_prime_number(n: int, t: int = 100) -> bool:
    """
    Performs the primarily test using Miller-Rabin's algorithm.
    See: https://github.com/sylhare/nprime/blob/master/nprime/pyprime.py

    :param n: (int) number on which the test is performed
    :param t: (int) number of round, by default equal to 100 the optimal number

    :return: (bool) True if n is a prime number, False otherwise
    """
    if n == 2:
        prime = True  # To normalize and make the algorythm works with 2
    else:
        prime = False  # All other even number will output false

    # Step 1: Have n-1 = 2^s * m (with m odd, and s number of twos factored)
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2  # d equals to quotient of d divided 2
        s += 1  # s > 1 when n is odd

    for _ in range(0, t):
        #  Step 2: test (a^d)^2^r ≡ 1 mod n for all r
        a = rd.randrange(1, n)
        for _ in range(0, s):
            x = pow(a, d * pow(2, s), n)
            if x == 1 or x == -1:
                prime = True  # Should be true for all a
            else:
                return False  # When not true, it's not prime for sure

    return prime  # /!\ Probable prime


class NotPrimerPowerException(Exception):
    """
    Exception raised when a non prime power is given to the following function.
    """
    pass


def primer_power(n: int) -> int:
    """
    Returns the prime number to write it in prime power.

    :param n: (int) the integer such as n = root^power with p a prime number

    :return: (int) the root

    :except NotPrimerPowerException: raised if the argument passed to the function is not a primer power
    """

    # n = root^power implies power <= log(n), so we iterate over all possible powers and check if the root is an integer
    for power in range(1, int(np.trunc(np.log(n))) + 1):
        root = int(np.trunc(np.power(n, 1./power)))
        if np.power(root, power) == n:
            if is_prime_number(root):
                return root
    raise NotPrimerPowerException


def gcd(x: int, y: int) -> int:
    """
    Computes the GCD (Greatest Common Divisor) of two numbers using Euclid's algorithm.

    :param x: (int) first number
    :param y: (int) second number

    :return: (int) the greatest common divider
    """
    if x < y:
        return gcd(y, x)
    while y != 0:
        (x, y) = (y, x % y)
    return x


def continued_fraction_expansion(n: int, b: int, q: int) -> int:
    """
    Extracts the period knowing the final state measured on the quantum computer at the end of Shor's algorithm
    execution. This extraction is performed using continued fraction expansion.

    :param n: (int) the integer we want to factorize
    :param b: (int) the measured state expressed in decimal base
    :param q: (int) the length of the first register use in Shor's algorithm

    :return: (int) the period researched in Shor's algorithm
    """

    # Initialize the float whose fractional expansion is looking for
    x = b/q

    # Compute the two first value of the expansion
    a_seq = [int(np.trunc(x))]
    if x == a_seq[-1]:
        raise ValueError('fail to find the period')
    x = 1 / (x - a_seq[-1])

    a_seq.append(int(np.trunc(x)))
    if x == a_seq[-1]:
        raise ValueError('fail to find the period')
    x = 1 / (x - a_seq[-1])

    # Init p and q sequences
    p_seq = [a_seq[0], a_seq[0] * a_seq[1] + 1]
    q_seq = [1, a_seq[1]]

    # Continue the expansion until the period i
    while q_seq[-1] < n:
        a_seq.append(int(np.trunc(x)))
        p_seq.append(a_seq[-1] * p_seq[-1] + p_seq[-2])
        q_seq.append(a_seq[-1] * q_seq[-1] + q_seq[-2])

        # If |b/q - p_n/q_n| < 1/q with q_n < n then r = q_n so the function returns the period
        if np.abs(b/q - p_seq[-1] / q_seq[-1]) < 1 / (2 * q):
            return q_seq[-1]

        if x == a_seq[-1]:
            raise ValueError('fail to find the period')
        x = 1/(x - a_seq[-1])

    # There is a non-zero probability that the algorithm fails to find the period because the measured state does no
    # match, in this case an exception is raised to indicate that the research must be continued
    raise ValueError('fail to find the period')
