# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
# =============================================================================

def calculate_sum(numbers):
    """Returns the sum of all numbers in the list (no built-in sum())."""
    total = 0
    for num in numbers:
        total += num
    return total


def calculate_average(numbers):
    """Returns the average of the numbers in the list."""
    return calculate_sum(numbers) / len(numbers)


def find_max(numbers):
    """Returns the largest number in the list (no built-in max())."""
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


def find_min(numbers):
    """Returns the smallest number in the list (no built-in min())."""
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest


def main():
    n = int(input("How many numbers? "))

    if n <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = []
    for i in range(1, n + 1):
        value = float(input(f"Enter number {i}: "))
        numbers.append(value)

    total = calculate_sum(numbers)
    average = calculate_average(numbers)
    maximum = find_max(numbers)
    minimum = find_min(numbers)

    # Print integers cleanly (no trailing .0) when the values are whole numbers
    def fmt(x):
        return int(x) if x == int(x) else x

    print("\nResults:")
    print(f"Sum:     {fmt(total)}")
    print(f"Average: {average}")
    print(f"Maximum: {fmt(maximum)}")
    print(f"Minimum: {fmt(minimum)}")


if __name__ == "__main__":
    main()
