def array_of_5_func():
    l = []
    for _ in range(5):
        l.append(int(input("Enter a number: ")))
    l.sort()
    print("Ascending order:", l)
    l.sort(reverse=True)
    print("Descending order:", l)
    return l

if __name__ == "__main__":
    array_of_5_func()
