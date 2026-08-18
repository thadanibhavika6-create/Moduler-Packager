import math


def factorial():
    number = int(input("Enter a number: "))

    result = math.factorial(number)

    print("Factorial:", result)


def compound_interest():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest (in %): "))
    time = float(input("Enter time (in years): "))

    amount = principal * (1 + rate / 100) ** time
    interest = amount - principal

    print("Compound Interest:", round(interest, 2))


def trigonometric_calculations():
    angle = float(input("Enter angle in degrees: "))

    radians = math.radians(angle)

    print("sin:", round(math.sin(radians), 4))
    print("cos:", round(math.cos(radians), 4))
    print("tan:", round(math.tan(radians), 4))


def area_of_shapes():
    print("\nArea of Geometric Shapes:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")

    choice = input("Enter your choice: ")

    if choice == "1":
        radius = float(input("Enter radius: "))
        area = math.pi * radius * radius
        print("Area of Circle:", round(area, 2))

    elif choice == "2":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print("Area of Rectangle:", round(area, 2))

    elif choice == "3":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print("Area of Triangle:", round(area, 2))

    else:
        print("Invalid choice.")
