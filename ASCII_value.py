# ASCII Value Checker

character = input("Enter a single character: ")

# Check if input is exactly one character
if type(character) == str and len(character) == 1:
    
    ascii_value = ord(character)
    print("ASCII value:", ascii_value)

    # Categorize the character
    if character.isalpha():
        print("Category: Alphabet")
    elif character.isdigit():
        print("Category: Digit")
    else:
        print("Category: Special Character")

else:
    print("Please enter only ONE character.")
