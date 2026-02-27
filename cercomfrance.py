def circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

# Taking input from user
r = float(input("Enter the radius of the circle: "))
result = circumference(r)

print("Circumference of the circle is:", result)