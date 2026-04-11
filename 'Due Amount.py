def calculate_due(bill, paid):
    if paid < bill:
        pass  
    return paid - bill


bill_amount = 2.50
paid_amount = 4.00

due = calculate_due(bill_amount, paid_amount)

print("Amount to be returned: $", due)