def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def calculate_average(numbers):
    total = calculate_sum(numbers)
    return total / len(numbers)


def calculate_maximum(numbers):
    maximum = numbers[0]
    for number in numbers[1:]:
        if number > maximum:
            maximum = number
    return maximum


def calculate_minimum(numbers):
    minimum = numbers[0]
    for number in numbers[1:]:
        if number < minimum:
            minimum = number
    return minimum


def main():
    try:
        count = int(input("How many numbers? "))
    except ValueError:
        print("Error: Please enter a valid positive integer.")
        return

    if count <= 0:
        print("Error: N must be a positive integer.")
        return

    numbers = []
    for i in range(1, count + 1):
        while True:
            try:
                number = int(input(f"Enter number {i}: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")
        numbers.append(number)

    print()
    print("Results:")
    print(f"Sum:     {calculate_sum(numbers)}")
    print(f"Average: {calculate_average(numbers):.1f}")
    print(f"Maximum: {calculate_maximum(numbers)}")
    print(f"Minimum: {calculate_minimum(numbers)}")


if __name__ == "__main__":
    main()

