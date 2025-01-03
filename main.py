from operations import Addition, Division, Multiplication, Soustraction


def main():
    print("Calculatrice simple")
    a, b = 10, 5
    print(f"Addition: {a} + {b} = {Addition.calculer(a, b)}")
    print(f"Soustraction: {a} - {b} = {Soustraction.calculer(a, b)}")
    print(f"Multiplication: {a} * {b} = {Multiplication.calculer(a, b)}")
    print(f"Division: {a} / {b} = {Division.calculer(a, b)}")

if __name__ == "__main__":
    main()