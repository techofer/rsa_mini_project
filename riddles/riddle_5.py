from rsa_functions import RSA


def riddle5():
    p = 7919
    q = 6841
    rsa = RSA.generate_from_primes(p=p, q=q)

    message = [ord(c) for c in "Hello world!"]
    encrypted = [rsa.encrypt(c) for c in message]
    print(
        f"original message: {message}, encrypted message: {encrypted}, public key: {rsa.public_key}"
    )


if __name__ == "__main__":
    riddle5()
