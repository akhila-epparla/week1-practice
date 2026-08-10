c_name=input("Enter customer name: ")
age=int(input("Enter customer age: "))
no_of_tickets=int(input("Enter number of tickets: "))
if age<12: 
    charge=120*no_of_tickets
elif age<=59:
    charge=200*no_of_tickets
else:
    charge=150*no_of_tickets
if no_of_tickets>=5:
    discount_percent=10
    discount_amount=charge*discount_percent/100
    final_charge=charge-discount_amount
else:
    discount_percent=0
    discount_amount=0
    final_charge=charge-discount_amount
print(f"Customer Name: {c_name}")
print(f"Ticket Price: ₹{charge/no_of_tickets}")
print(f"Number of tickets: {no_of_tickets}")
print(f"Total Before Discount: ₹{charge}")
print(f"Discount ({discount_percent}%): ₹{discount_amount}")
print(f"Final Amount: ₹{final_charge}")