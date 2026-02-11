num = int(input("Enter a decimal number: "))

if num == 0:
    print("Binary number: 0")
else:
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2

    print("Binary number:", binary)

