seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]
for i in range(1,len(seats)):
    if(seats[i]=="Available"):
        print(f"Seat {i}: Available")
    else:
        print(f"Seat {i}: Booked")
seat_number=int(input("Enter seat number: "))
if(seats[seat_number]=="Available"):
    print("Seat booked successfully.")
    seats[seat_number]="Booked"
else:
    print("Seat is already booked.")
total=len(seats)
available=seats.count("Available")
booked=seats.count("Booked")
print(f"Total seats: {total}")
print(f"Available seats: {available}")
print(f"Booked seats: {booked}")