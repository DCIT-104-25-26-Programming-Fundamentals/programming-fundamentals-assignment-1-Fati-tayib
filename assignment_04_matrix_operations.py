# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
# =============================================================================

def read_matrix(rows, cols, label=""):
    """
    Reads a matrix of the given size from the user.
    Each row is entered on one line, values separated by spaces.
    """
    matrix = []
    for i in range(rows):
        while True:
            raw = input(f"Enter row {i + 1}{label}: ").split()
            row = [int(x) for x in raw]
            if len(row) != cols:
                print(f"Error: expected {cols} values, got {len(row)}. Try again.")
                continue
            matrix.append(row)
            break
    return matrix


def print_matrix(matrix, title="Matrix"):
    """Displays a matrix in a neat, aligned grid format."""
    print(f"\n{title}:")

    # Find the widest element for column alignment
    width = 0
    for row in matrix:
        for value in row:
            width = max(width, len(str(value)))

    for row in matrix:
        line = "  ".join(str(value).rjust(width) for value in row)
        print(line)


def transpose(matrix):
    """Returns the transpose of a matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(a, b):
    """Returns the element-wise sum of two same-sized matrices."""
    rows = len(a)
    cols = len(a[0])

    result = [[0] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]

    return result


def multiply_matrices(a, b):
    """
    Returns the matrix product A x B.
    A is M x N, B is N x P, result is M x P.
    """
    m = len(a)
    n = len(a[0])
    p = len(b[0])

    result = [[0] * p for _ in range(m)]

    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            result[i][j] = total

    return result


def part_a_transpose():
    print("\n--- PART A: Transpose a Matrix ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, cols)
    result = transpose(matrix)

    print_matrix(matrix, "Original Matrix")
    print_matrix(result, "Transposed Matrix")


def part_b_addition():
    print("\n--- PART B: Add Two Matrices ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("\nMatrix A:")
    a = read_matrix(rows, cols)

    print("\nMatrix B:")
    b = read_matrix(rows, cols)

    result = add_matrices(a, b)

    print_matrix(a, "Matrix A")
    print_matrix(b, "Matrix B")
    print_matrix(result, "Sum (A + B)")


def part_c_multiplication():
    print("\n--- PART C: Multiply Two Matrices ---")
    m = int(input("Enter number of rows for Matrix A: "))
    n = int(input("Enter number of columns for Matrix A (= rows for Matrix B): "))
    p = int(input("Enter number of columns for Matrix B: "))

    print("\nMatrix A:")
    a = read_matrix(m, n)

    print("\nMatrix B:")
    b = read_matrix(n, p)

    result = multiply_matrices(a, b)

    print_matrix(a, "Matrix A")
    print_matrix(b, "Matrix B")
    print_matrix(result, "Product (A x B)")


def main():
    part_a_transpose()
    part_b_addition()
    part_c_multiplication()


if __name__ == "__main__":
    main()
