from random import randrange


def extended_gcd(a: int, b: int):
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

        return d, y, x - y*q

    elif b > a:
        d, x, y = extended_gcd(b, a)
        return d, y, x
    else:
        return a, 1, 0


def modular_inverse(a, n):
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
        return x
    else:
        return None


def modular_exponent(a, d, n):
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
    binary_d = int(binary_str_d[2:])
    counter = 0
    multi = 1
    a_mod_n = a % n
    while binary_d:
        power = binary_d % 10 * 2 ** counter
        multi *= (a_mod_n ** power) % n
        multi = multi % n
        counter += 1
        binary_d = binary_d // 10
    multi = multi % n
    return multi



def miller_rabin(n):
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


def is_prime(n):
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


def generate_prime(digits):
    for i in range(digits * 10):
        n = randrange(10 ** (digits - 1), 10 ** digits)
        if is_prime(n):
            return n
    return None

if __name__ == "__main__":
    print(modular_inverse(8, 143))
