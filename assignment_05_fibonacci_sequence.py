def generate_fibonacci_terms(n):
    if n <= 0:
        return []

    sequence = []
    first, second = 0, 1
    for _ in range(n):
        sequence.append(first)
        first, second = second, first + second
    return sequence


def is_fibonacci(number):
    if number < 0:
        return False
    if number == 0 or number == 1:
        return True

    first, second = 0, 1
    while second < number:
        first, second = second, first + second

    return number == first or number == second


def main():
    try:
        terms = int(input("How many terms? "))
    except ValueError:
        print("Error: Please enter a positive integer.")
        return

    if terms <= 0:
        print("Error: Please enter a positive integer.")
        return

    fibonacci_sequence = generate_fibonacci_terms(terms)
    print("Fibonacci sequence:", end=" ")
    print(*fibonacci_sequence)

    try:
        value = int(input("Enter a number to check: "))
    except ValueError:
        print("Error: Please enter a valid integer.")
        return

    if is_fibonacci(value):
        print(f"{value} is a Fibonacci number.")
    else:
        print(f"{value} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()

