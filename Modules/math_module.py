def multiplication_table(number, limit=5):
    """
    Generate a multiplication table for a given number.
    Args:
        number (int): The number to create the multiplication table for
        limit (int): The upper limit of the multiplication table (default=5)
    Returns:
        list: List of tuples containing (number, multiplier, result)
    """
    results = []
    for i in range(1, limit + 1):
        result = number * i
        print(f"{number} x {i} = {result}")
        results.append((number, i, result))
    return results
