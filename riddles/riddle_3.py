from number_theory_functions import modular_inverse
from rsa_functions import RSA


def riddle3():
    n = 12215009
    e = 3499

    public_key = (n, e)

    encrypted = 42

    # according to https://davidson-web2.weizmann.ac.il/davidson1/applets/factor.htm : 12215009 = 3491 * 3499
    p = 3491
    q = 3499
    fi_n = (p - 1) * (q - 1)
    private_key = (n, modular_inverse(e, fi_n))

    rsa = RSA(public_key=public_key, private_key=private_key)

    decrypted = rsa.decrypt(encrypted)
    print(f"private key: {private_key}, decrypted: {decrypted}")


if __name__ == "__main__":
    riddle3()
