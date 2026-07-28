def read_matrix():
    try:
        rows = int(input("Enter number of rows: "))
        cols = int(input("Enter number of columns: "))
    except ValueError:
        print("Invalid dimensions.")
        return None

    if rows <= 0 or cols <= 0:
        print("Dimensions must be positive.")
        return None

    matrix = []
    for i in range(rows):
        while True:
            try:
                values = list(map(int, input(f"Enter row {i + 1}: ").split()))
                if len(values) != cols:
                    print(f"Please enter exactly {cols} values.")
                    continue
                matrix.append(values)
                break
            except ValueError:
                print("Please enter only integers.")
    return matrix


def print_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:>6}", end="")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    return [[matrix[row][col] for row in range(rows)] for col in range(cols)]


def add_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        return None

    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[i])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return None

    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            total = 0
            for k in range(len(matrix_b)):
                total += matrix_a[i][k] * matrix_b[k][j]
            row.append(total)
        result.append(row)
    return result


def main():
    print("Matrix Operations")
    print("1. Transpose matrix")
    print("2. Add two matrices")
    print("3. Multiply two matrices")
    print("4. Quit")

    choice = input("Choose an operation (1-4): ").strip()

    if choice == "1":
        matrix = read_matrix()
        if matrix is None:
            return
        print("\nOriginal Matrix:")
        print_matrix(matrix)
        print("\nTransposed Matrix:")
        print_matrix(transpose_matrix(matrix))
    elif choice == "2":
        print("Enter matrix A:")
        matrix_a = read_matrix()
        if matrix_a is None:
            return
        print("Enter matrix B:")
        matrix_b = read_matrix()
        if matrix_b is None:
            return
        result = add_matrices(matrix_a, matrix_b)
        if result is None:
            print("Matrices must have the same dimensions.")
        else:
            print("\nResult:")
            print_matrix(result)
    elif choice == "3":
        print("Enter matrix A:")
        matrix_a = read_matrix()
        if matrix_a is None:
            return
        print("Enter matrix B:")
        matrix_b = read_matrix()
        if matrix_b is None:
            return
        result = multiply_matrices(matrix_a, matrix_b)
        if result is None:
            print("The number of columns in matrix A must equal the number of rows in matrix B.")
        else:
            print("\nResult:")
            print_matrix(result)
    elif choice == "4":
        print("Goodbye!")
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()

