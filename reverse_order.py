num = input("Enter a number: ")

if num[0] == '-':
    num = num[1:]

digit_count = len(num)

print("Total number of digits:", digit_count)
