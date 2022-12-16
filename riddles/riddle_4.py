from number_theory_functions import extended_gcd, modular_inverse

e = 11
N = 991
fi_991 = 990
if extended_gcd(11, N)[0] == 1:
    print(modular_inverse(e, fi_991))

# x^(ed) % N = x
# ed = 990 * k + 1

