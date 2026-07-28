# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 1
# Topic: Conditional Logic, Loops, and Functions
# =============================================================================
#
# TASK: Prime Number Checker
# =============================================================================

def is_prime(n):
    """
    Returns True if n is a prime number, False otherwise.
    A prime number is a whole number greater than 1 that has no divisors
    other than 1 and itself.
    """
    # Numbers less than 2 are NOT prime
    if n < 2:
        return False

    # Check for divisors from 2 up to the square root of n
    # (no need to check beyond that, since factors pair up)
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


def main():
    number = int(input("Enter a number: "))

    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is NOT a prime number.")


if __name__ == "__main__":
    main()
