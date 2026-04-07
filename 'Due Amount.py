def calculate_due_amount(bill, paid):
    return paid - bill   

try:
    bill = float(input("Enter total bill amount: "))
    paid = float(input("Enter amount paid: "))

    if paid < bill:
        print("Insufficient payment! Customer still owes money.")
    else:
        due = calculate_due_amount(bill, paid)
        print("Amount to be returned:", due)

except ValueError:
    print("Error! Please enter valid numeric values.")