from random import randrange
from typing import Optional, Tuple


def extended_gcd(a: int, b: int) -> Tuple[int, int, int]:
    """
    Returns the extended gcd of a and b

    Parameters
    ----------
    a : Input data.
    b : Input data.
    Returns
    -------
    (d, x, y): d = gcd(a,b) = a*x + b*y
    """

    if a > b:
        q = a // b
        r = a % b

        if r == 0:
            return b, 0, 1

        d, x, y = extended_gcd(b, r)

        return d, y, x - y * q

    elif b > a:
        d, x, y = extended_gcd(b, a)
        return d, y, x
    else:
        return a, 1, 0


def modular_inverse(a: int, n: int) -> Optional[int]:
    """
    Returns the inverse of a modulo n if one exists

    Parameters
    ----------
    a : Input data.
    n : Input data.

    Returns
    -------
    x: such that (a*x % n) == 1 and 0 <= x < n if one exists, else None
    """
    d, x, y = extended_gcd(a, n)
    if d == 1:
        return x % n
    else:
        return None


def modular_exponent(a: int, d: int, n: int) -> int:
    """
    Returns a to the power of d modulo n

    Parameters
    ----------
    a : The exponential's base.
    d : The exponential's exponent.
    n : The exponential's modulus.

    Returns
    -------
    b: such that b == (a**d) % n
    """
    binary_str_d = bin(d)
    binary_d = list(binary_str_d[2:])
    counter = 0
    multi = 1
    temp = a % n
    while len(binary_d) > counter:
        multi *= temp ** (int(binary_d[-(counter + 1)])) % n
        multi = multi % n
        temp = temp**2 % n
        counter += 1

    return multi % n


def miller_rabin(n: int) -> bool:
    """
    Checks the primality of n using the Miller-Rabin test

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a 3/4 chance at least to be False
    """
    a = randrange(1, n)
    k = 0
    d = n - 1
    while d % 2 == 0:
        k = k + 1
        d = d // 2
    x = modular_exponent(a, d, n)
    if x == 1 or x == n - 1:
        return True
    for _ in range(k):
        x = (x * x) % n
        if x == 1:
            return False
        if x == n - 1:
            return True
    return False


def is_prime(n: int) -> bool:
    """
    Checks the primality of n

    Parameters
    ----------
    n : The number to check

    Returns
    -------
    b: If n is prime, b is guaranteed to be True.
    If n is not a prime, b has a chance of less than 1e-10 to be True
    """
    for _ in range(10):
        if not miller_rabin(n):
            return False
    return True


def generate_prime(digits: int) -> Optional[int]:
    for i in range(digits * 10):
        n = randrange(10 ** (digits - 1), 10**digits)
        if is_prime(n):
            return n
    return None


if __name__ == "__main__":
    print(modular_inverse(8, 143))
