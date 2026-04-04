
n = int(input("Enter a number: "))

odd_numbers = [i for i in range(1, n) if i % 2 != 0]

odd_cubes = [i**3 for i in odd_numbers]

roots = [round(math.sqrt(i), 2) for i in odd_numbers]

capitalized_list = [str(i).capitalize() for i in odd_numbers]

print("Odd Numbers:", odd_numbers)
print("Cubes of Odd Numbers:", odd_cubes)
print("Square Roots:", roots)
print("Capitalized List:", capitalized_list)