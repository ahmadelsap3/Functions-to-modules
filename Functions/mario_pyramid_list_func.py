def print_pyramid():
    rows = int(input("Enter the number of rows for the pyramid: "))
    l = [" "] * rows
    for _ in range(rows):
        l.append("*")
        l.pop(0)
        print("".join(l))

if __name__ == "__main__":
    print_pyramid()
