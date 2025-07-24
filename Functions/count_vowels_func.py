def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
            print(f"Found vowel: {char}")
    print(f"Total number of vowels: {count}")
    return count

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    count_vowels(user_input)
