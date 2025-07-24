def multiplication_table():
    number = int(input("Enter a number: "))
    for i in range(1, 6):
        result = number * i
        print(f"{number} x {i} = {result}")

if __name__ == "__main__":
    multiplication_table()
