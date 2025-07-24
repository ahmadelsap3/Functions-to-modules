def count_vowels(text):
    """
    Count and print the number of vowels in a given string.
    Args:
        text (str): The input string to analyze
    Returns:
        int: The total number of vowels found
    """
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
            print(f"Found vowel: {char}")
    print(f"Total number of vowels: {count}")
    return count

def find_i_locations(text):
    """
    Find all occurrences of the letter 'i' (case insensitive) in a string.
    Args:
        text (str): The input string to search
    Returns:
        list: List of indices where 'i' was found
    """
    locations = []
    for i in range(len(text)):
        if text[i].lower() == 'i':
            locations.append(i)
    return locations
