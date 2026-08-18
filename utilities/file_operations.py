def create_file():
    filename = input("Enter file name: ")

    with open(filename, "w") as file:
        pass

    print("File created successfully!")


def write_file():
    filename = input("Enter file name: ")
    data = input("Enter data to write: ")

    with open(filename, "w") as file:
        file.write(data)

    print("Data written successfully!")


def read_file():
    filename = input("Enter file name: ")

    with open(filename, "r") as file:
        data = file.read()

    print("File Content:")
    print(data)


def append_file():
    filename = input("Enter file name: ")
    data = input("Enter data to append: ")

    with open(filename, "a") as file:
        file.write(data)

    print("Data appended successfully!")
