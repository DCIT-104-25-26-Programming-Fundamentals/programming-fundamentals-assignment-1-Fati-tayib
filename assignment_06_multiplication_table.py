# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 6
# Topic: Loops and Functions
# =============================================================================
#
# TASK: Multiplication Table Generator
# =============================================================================

def print_table(number):
    """Prints the multiplication table for a single number, from 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        product = number * i
        print(f"{number}  x  {i:<2} =  {product}")


def part_a_single_table():
    """Part A: Ask for a number and print its multiplication table."""
    number = int(input("Enter a number: "))
    print_table(number)


def print_tables_up_to_n(n):
    """Prints multiplication tables for every number from 1 to N,
    separated by a line of dashes."""
    for number in range(1, n + 1):
        print_table(number)
        print("-" * 29)


def part_b_tables_up_to_n():
    """Part B: Ask for N and print tables for every number from 1 to N."""
    n = int(input("Enter a number (N): "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    print_tables_up_to_n(n)


def main():
    part_a_single_table()
    print()
    part_b_tables_up_to_n()


if __name__ == "__main__":
    main()
