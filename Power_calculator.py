n = int(input("How many numbers will you enter? "))

count = 0

for i in range(n):
    num = int(input("Enter a number: "))
    count = count + 1

print("Total numbers entered:", count)