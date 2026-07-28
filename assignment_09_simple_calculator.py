# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 9
# =============================================================================
#
# TASK: Console-Based Simple Calculator
# =============================================================================

def add(a, b):
    """Returns the sum of a and b."""
    return a + b


def subtract(a, b):
    """Returns the difference of a and b."""
    return a - b


def multiply(a, b):
    """Returns the product of a and b."""
    return a * b


def divide(a, b):
    """
    Returns a / b, rounded to 2 decimal places.
    Returns None if b is zero (caller must handle this case).
    """
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """
    Returns the remainder of a % b.
    Returns None if b is zero (caller must handle this case).
    """
    if b == 0:
        return None
    return a % b


def exponentiate(a, b):
    """Returns a raised to the power of b."""
    return a ** b


def display_menu():
    """Prints the calculator menu."""
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_numbers():
    """Prompts for and returns two numbers from the user."""
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    return a, b


def fmt(x):
    """Formats a number without a trailing .0 for whole-number results."""
    return int(x) if x == int(x) else x


def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus),
        "6": ("**", exponentiate),
    }

    while True:
        display_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Error: Invalid choice. Please select a number from 1 to 7.")
            print()
            continue

        symbol, operation = operations[choice]
        a, b = get_numbers()

        if choice in ("4", "5") and b == 0:
            if choice == "4":
                print("Error: Cannot divide by zero.")
            else:
                print("Error: Cannot perform modulus with zero.")
            print()
            continue

        result = operation(a, b)
        print(f"Result: {fmt(a)} {symbol} {fmt(b)} = {fmt(result)}")
        print()


if __name__ == "__main__":
    main()
