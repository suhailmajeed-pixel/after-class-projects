try:
    age = input("Enter your age: ")

    age = int(age)

    if age <= 0:
        print("Invalid age! Age must be a positive number.")

    else:
        if age % 2 == 0:
            print("Your age is Even.")
        else:
            print("Your age is Odd.")

except ValueError:
    print("Error! Please enter a valid integer value (no decimals, letters, or special characters).")