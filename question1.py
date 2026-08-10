parking_hours=int(input("Enter parking hours: "))
if parking_hours<=2:
    p_charge=parking_hours*30
elif(parking_hours<=5):
    p_charge=parking_hours*25
else:
    p_charge=parking_hours*20
if p_charge>=150:
    s_charge=20
    final_charge=s_charge+p_charge
else:
    s_charge=0
    final_charge=s_charge+p_charge
print(f"Parking charge: ₹{p_charge}")
print(f"Service charge: ₹{s_charge}")
print(f"Final Amount: ₹{final_charge}")