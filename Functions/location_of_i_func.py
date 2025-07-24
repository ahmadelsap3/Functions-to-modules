def find_locations_of_i(input_string):
    locations = []
    for i in range(len(input_string)):
        if input_string[i] == 'i' or input_string[i] == 'I':
            locations += [i]
    return locations

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    print("Locations of 'i':", find_locations_of_i(user_input))
