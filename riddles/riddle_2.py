from number_theory_functions import modular_exponent


def riddle2():
    print(
        modular_exponent(456456, modular_exponent(7896543, 74365753, 400), 1000) // 100
    )


if __name__ == "__main__":
    riddle2()
