base = int(input("Enter the base number: "))
power = int(input("Enter the power: "))

result = 1
i = 0

while i < power:
    result = result * base
    i += 1

print("Result:", result)

