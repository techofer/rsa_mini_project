from __future__ import annotations

import random
from typing import Optional, Tuple

import number_theory_functions


class RSA:
    def __init__(
        self, public_key: Tuple[int, int], private_key: Optional[Tuple[int, int]] = None
    ):
        self.public_key: Tuple[int, int] = public_key
        self.private_key: Optional[Tuple[int, int]] = private_key

    @staticmethod
    def _generate(p: int, q: int) -> RSA:
        n = p * q

        fi_n = (p - 1) * (q - 1)
        e = fi_n
        # make sure that e ∈ Uφ(N)
        while number_theory_functions.extended_gcd(e, fi_n)[0] != 1:
            # 2 <= e <= fi_n
            e = random.randint(2, fi_n)
        d = number_theory_functions.modular_inverse(e, fi_n)
        if d is None:
            raise Exception(f"Failed to inverse {e}")
        return RSA(public_key=(n, e), private_key=(n, d))

    @staticmethod
    def generate_from_primes(p: int, q: int) -> RSA:
        if not (
            number_theory_functions.is_prime(q) and number_theory_functions.is_prime(q)
        ):
            raise Exception(f"p ({p}) or q ({q}) are not prime!")
        return RSA._generate(p=p, q=q)

    @staticmethod
    def generate(digits: int = 10) -> RSA:
        """
        Creates an RSA encryption system object

        Parameters
        ----------
        digits : The number of digits N should have

        Returns
        -------
        RSA: The RSA system containing:
        * The public key (N,e)
        * The private key (N,d)
        """
        n = 0
        p = 0
        q = 0

        while len(str(n)) != digits:
            p_digits = random.randint(1, digits)
            q_digits = digits - p_digits
            p = number_theory_functions.generate_prime(p_digits)
            q = number_theory_functions.generate_prime(q_digits)
            if q is None or p is None:
                continue

            n = p * q

        return RSA._generate(p=p, q=q)

    def encrypt(self, m: int) -> int:
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        return number_theory_functions.modular_exponent(
            m, d=self.public_key[1], n=self.public_key[0]
        )

    def decrypt(self, c: int) -> int:
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
        """
        if self.private_key is None:
            raise Exception("private key not provided")
        return number_theory_functions.modular_exponent(
            c, d=self.private_key[1], n=self.private_key[0]
        )
