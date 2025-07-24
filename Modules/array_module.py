def array_sort():
    """
    Function to input 5 numbers and sort them in ascending and descending order.
    Returns the sorted array.
    """
    numbers = []
    for _ in range(5):
        numbers.append(int(input("Enter a number: ")))
    
    # Ascending sort
    ascending = sorted(numbers)
    print("Ascending order:", ascending)
    
    # Descending sort
    descending = sorted(numbers, reverse=True)
    print("Descending order:", descending)
    
    return numbers
