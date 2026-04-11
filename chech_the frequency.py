test_dict = {
    "codingal": 3,
    "is": 2,
    "Best": 2,
    "4": 2,
    "coding": 1
}

print("Test Dictionary:", test_dict)

value = int(input("Enter the value to check frequency: "))

count = 0
for key in test_dict:
    if test_dict[key] == value:
        count += 1

print("Frequency (number of occurrences) of value", value, "is:", count)