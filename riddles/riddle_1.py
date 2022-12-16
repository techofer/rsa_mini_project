# given that loki doesn't care to lose his money, it is possible :)
from number_theory_functions import extended_gcd, modular_inverse


def riddle1():
    print(extended_gcd(911, 7879))
    print(911 * (7879 - 2733) * 1000000 + 7879 * (-911 + 316) * 1000000)
    print(modular_inverse(8, 143))
    # we found the extended GCD of the given numbers. we added and substructed the product of the numbers to get the desired output.


if __name__ == "__main__":
    riddle1()
