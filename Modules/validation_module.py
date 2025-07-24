def validate_name(name):
    """
    Validate if a name contains only alphabetic characters and is not empty.
    Args:
        name (str): The name to validate
    Returns:
        bool: True if valid, False otherwise
    """
    return name.isalpha() and name.strip() != ""

def validate_email(email):
    """
    Validate basic email format.
    Args:
        email (str): The email address to validate
    Returns:
        bool: True if valid, False otherwise
    """
    if "@" not in email or "." not in email:
        return False
    
    if email[0] in ["@", "."] or email[-1] in ["@", "."]:
        return False
    
    if "@." in email or ".@" in email:
        return False
    
    return True

def validate_user_input():
    """
    Interactive function to validate user's name and email input.
    Returns:
        tuple: (name, email) if both are valid
    """
    name = input("Enter your name: ")
    while not validate_name(name):
        print("Invalid name. Please enter a valid name (alphabetic characters only).")
        name = input("Enter your name: ")

    email = input("Enter your email: ")
    while not validate_email(email):
        print("Invalid email. Please enter a valid email address.")
        email = input("Enter your email: ")

    return name, email
