def print_single_table(number):
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number}  x  {i}  =  {number * i}")
    print()


def print_tables_up_to(n):
    for value in range(1, n + 1):
        print_single_table(value)
        if value < n:
            print("-" * 27)


def main():
    try:
        n = int(input("Enter a number: "))
    except ValueError:
        print("Error: Please enter a positive integer.")
        return

    if n <= 0:
        print("Error: Please enter a positive integer.")
        return

    print_single_table(n)
    print("Tables from 1 to N:")
    print_tables_up_to(n)


if __name__ == "__main__":
    main()

