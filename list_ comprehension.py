n = int(input("Enter a number: "))

odd_numbers = [i for i in range(1, n) if i % 2 != 0]

odd_numbers_map = list(map(lambda x: x, [i for i in range(1, n) if i % 2 != 0]))

fruits = ["apple", "banana", "cherry", "mango", "orange"]

capitalized_fruits = [fruit.capitalize() for fruit in fruits]

print("Odd numbers (list comprehension):", odd_numbers)
print("Odd numbers (using map):", odd_numbers_map)
print("Capitalized fruits:", capitalized_fruits)