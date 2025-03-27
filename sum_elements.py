# A refactored program to sum user-provided integers with improved readability and error handling.

MAX_ELEMENTS = 100

def calculate_sum(numbers):
    """Calculate the sum of a list of numbers."""
    return sum(numbers)

def get_number_of_elements():
    """Prompt the user for the number of elements to sum."""
    while True:
        try:
            n = int(input(f"Enter the number of elements (1-{MAX_ELEMENTS}): "))
            if 1 <= n <= MAX_ELEMENTS:
                return n
            else:
                print(f"Invalid input. Please enter a number between 1 and {MAX_ELEMENTS}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_elements(n):
    """Prompt the user to input `n` integers."""
    numbers = []
    print(f"Enter {n} integers:")
    for i in range(n):
        while True:
            try:
                num = int(input(f"Element {i + 1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")
    return numbers

def main():
    """Main function to execute the program."""
    try:
        while True:
            n = get_number_of_elements()
            numbers = get_elements(n)
            total = calculate_sum(numbers)
            print("Sum of the numbers:", total)

            # Ask the user if they want to perform another calculation
            again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if again not in ('yes', 'y'):
                print("Goodbye!")
                break
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit(1)

if __name__ == "__main__":
    main()
