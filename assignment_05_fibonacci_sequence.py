# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 5
# Topic: Loops, Sequences, and Functions
# =============================================================================
#
# TASK: Fibonacci Sequence Generator
# =============================================================================

def generate_fibonacci(n):
    """
    Returns a list containing the first n terms of the Fibonacci sequence,
    generated using a loop (not recursion).
    """
    sequence = []
    a, b = 0, 1

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence


def print_first_n_terms():
    """Part A: Prints the first N terms of the Fibonacci sequence."""
    n = int(input("How many terms? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    sequence = generate_fibonacci(n)
    terms = " ".join(str(term) for term in sequence)
    print(f"Fibonacci sequence: {terms}")


def is_fibonacci(number):
    """
    Part B logic: Returns True if the given number appears in the
    Fibonacci sequence, generated using a loop (not recursion).
    """
    if number < 0:
        return False

    a, b = 0, 1
    while a <= number:
        if a == number:
            return True
        a, b = b, a + b

    return False


def check_number():
    """Part B: Asks for a number and checks if it's a Fibonacci number."""
    number = int(input("Enter a number to check: "))

    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")


def main():
    print_first_n_terms()
    check_number()


if __name__ == "__main__":
    main()
