#!/usr/bin/env python3
"""
Main program demonstrating the use of custom Python modules
"""

import sys
import os

# Add the modules directory to the Python path
sys.path.append(os.path.dirname(__file__))

from array_module import array_sort
from string_module import count_vowels, find_i_locations
from pyramid_module import create_pyramid, create_pyramid_list
from math_module import multiplication_table
from validation_module import validate_name, validate_email, validate_user_input

def main():
    while True:
        print("\n=== Python Modules Demo ===")
        print("1. Sort array of 5 numbers")
        print("2. Analyze text (vowels and 'i' locations)")
        print("3. Create pyramids")
        print("4. Generate multiplication table")
        print("5. Validate name and email")
        print("0. Exit")
        
        choice = input("\nEnter your choice (0-5): ")
        
        if choice == '0':
            break
            
        elif choice == '1':
            print("\n--- Array Sorting ---")
            array_sort()
            
        elif choice == '2':
            print("\n--- Text Analysis ---")
            text = input("Enter a text to analyze: ")
            print("\nCounting vowels:")
            count_vowels(text)
            print("\nFinding 'i' locations:")
            locations = find_i_locations(text)
            print(f"Letter 'i' found at positions: {locations}")
            
        elif choice == '3':
            print("\n--- Pyramid Creation ---")
            rows = int(input("Enter number of rows: "))
            print("\nRegular pyramid:")
            create_pyramid(rows)
            print("\nList-based pyramid:")
            create_pyramid_list(rows)
            
        elif choice == '4':
            print("\n--- Multiplication Table ---")
            number = int(input("Enter a number: "))
            limit = int(input("Enter the table limit (default=5): ") or "5")
            multiplication_table(number, limit)
            
        elif choice == '5':
            print("\n--- Input Validation ---")
            print("\nTesting name validation:")
            test_name = input("Enter a name to validate: ")
            if validate_name(test_name):
                print("Valid name!")
            else:
                print("Invalid name!")
                
            print("\nTesting email validation:")
            test_email = input("Enter an email to validate: ")
            if validate_email(test_email):
                print("Valid email!")
            else:
                print("Invalid email!")
                
            print("\nInteractive validation:")
            name, email = validate_user_input()
            print("Validated input:")
            print(f"Name: {name}")
            print(f"Email: {email}")
            
        else:
            print("Invalid choice! Please try again.")
    
    print("\nThank you for using the Python Modules Demo!")

if __name__ == "__main__":
    main()
