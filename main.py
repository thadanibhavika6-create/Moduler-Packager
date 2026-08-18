import datetime
import time
import math
import random
import uuid

from utilities import file_operations
from utilities import math_operations


def datetime_menu():

    while True:
        print("\n--- Date and Time Operations ---")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            current = datetime.datetime.now()
            print("Current Date and Time:", current.strftime("%Y-%m-%d %H:%M:%S"))

        elif choice == "2":
            date1 = input("Enter the first date (YYYY-MM-DD): ")
            date2 = input("Enter the second date (YYYY-MM-DD): ")

            d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

            difference = abs((d2 - d1).days)

            print("Difference:", difference, "days")

        elif choice == "3":
            date_text = input("Enter date (YYYY-MM-DD): ")

            date = datetime.datetime.strptime(date_text, "%Y-%m-%d")

            print("Formatted Date:", date.strftime("%d-%m-%Y"))

        elif choice == "4":
            input("Press Enter to start stopwatch...")
            start = time.time()

            input("Press Enter to stop stopwatch...")
            end = time.time()

            print("Elapsed Time:", round(end - start, 2), "seconds")

        elif choice == "5":
            seconds = int(input("Enter countdown time in seconds: "))

            while seconds > 0:
                print("Time left:", seconds, "seconds")
                time.sleep(1)
                seconds -= 1

            print("Countdown finished!")

        elif choice == "6":
            break

        else:
            print("Invalid choice.")


def random_menu():

    while True:
        print("\n--- Random Data Generation ---")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = random.randint(1, 100)
            print("Random Number:", number)

        elif choice == "2":
            numbers = [random.randint(1, 100) for _ in range(5)]
            print("Random List:", numbers)

        elif choice == "3":
            length = int(input("Enter password length: "))

            characters = (
                "abcdefghijklmnopqrstuvwxyz"
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                "0123456789"
                "!@#$%^&*"
            )

            password = "".join(
                random.choice(characters) for _ in range(length)
            )

            print("Generated Password:", password)

        elif choice == "4":
            otp = random.randint(100000, 999999)
            print("Generated OTP:", otp)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def uuid_operation():

    print("\n--- Generate Unique Identifiers ---")

    unique_id = uuid.uuid4()

    print("Generated UUID:", unique_id)


def explore_module():

    print("\n--- Explore Module Attributes ---")

    module_name = input("Enter module name to explore: ")

    try:
        if module_name == "math":
            module = math
        elif module_name == "random":
            module = random
        elif module_name == "datetime":
            module = datetime
        elif module_name == "time":
            module = time
        elif module_name == "uuid":
            module = uuid
        else:
            print("Module not available.")
            return

        attributes = dir(module)

        print("Available Attributes:")
        print(attributes)

    except Exception as e:
        print("Error:", e)


def math_menu():

    while True:
        print("\n--- Mathematical Operations ---")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            math_operations.factorial()

        elif choice == "2":
            math_operations.compound_interest()

        elif choice == "3":
            math_operations.trigonometric_calculations()

        elif choice == "4":
            math_operations.area_of_shapes()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def file_menu():

    while True:
        print("\n--- File Operations ---")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_operations.create_file()

        elif choice == "2":
            file_operations.write_file()

        elif choice == "3":
            file_operations.read_file()

        elif choice == "4":
            file_operations.append_file()

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


def main():

    while True:

        print("\n============================")
        print(" Welcome to Multi-Utility Toolkit")
        print("============================")

        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            datetime_menu()

        elif choice == "2":
            math_menu()

        elif choice == "3":
            random_menu()

        elif choice == "4":
            uuid_operation()

        elif choice == "5":
            file_menu()

        elif choice == "6":
            explore_module()

        elif choice == "7":
            print("\nThank you for using the Multi-Utility Toolkit!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()