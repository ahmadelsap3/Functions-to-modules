def create_pyramid(rows):
    """
    Print a right-aligned pyramid with the specified number of rows.
    Args:
        rows (int): Number of rows in the pyramid
    """
    for i in range(1, rows + 1):
        print(" " * (rows - i) + "*" * i)

def create_pyramid_list(rows):
    """
    Create and print a right-aligned pyramid using list operations.
    Args:
        rows (int): Number of rows in the pyramid
    """
    spaces = [" "] * rows
    for _ in range(rows):
        spaces.append("*")
        spaces.pop(0)
        print("".join(spaces))
