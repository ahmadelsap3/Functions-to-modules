def print_pyramid():
    rows = int(input("Enter the number of rows for the pyramid: "))
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)

if __name__ == "__main__":
    print_pyramid()
