from __future__ import annotations
import random

from typing import Optional, Tuple
import number_theory_functions


class RSA:
    def __init__(
        self, public_key: Tuple[int, int], private_key: Optional[Tuple[int, int]] = None
    ):
        self.public_key: Tuple[int, int] = public_key
        self.private_key: Tuple[int, int] = private_key

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
        p = number_theory_functions.generate_prime(digits)
        q = number_theory_functions.generate_prime(digits)
        n = p * q

        fi_n = (p - 1) * (q - 1)
        e = fi_n
        # make sure that e ∈ Uφ(N)
        while number_theory_functions.extended_gcd(e, fi_n) != 1:
            # 2 <= e <= fi_n
            e = random.randint(2, fi_n)
        d = number_theory_functions.modular_inverse(e, fi_n)
        return RSA(public_key=(n, e), private_key=(n, d))

    def encrypt(self, m: str) -> str:
        """
        Encrypts the plaintext m using the RSA system

        Parameters
        ----------
        m : The plaintext to encrypt

        Returns
        -------
        c : The encrypted ciphertext
        """
        return "".join(
            [
                chr(number_theory_functions.modular_exponent(ord(c), *self.public_key))
                for c in m
            ]
        )

    def decrypt(self, c: str) -> str:
        """
        Decrypts the ciphertext c using the RSA system

        Parameters
        ----------
        c : The ciphertext to decrypt

        Returns
        -------
        m : The decrypted plaintext
        """
        return "".join(
            [
                chr(number_theory_functions.modular_exponent(ord(c), *self.private_key))
                for c in c
            ]
        )
