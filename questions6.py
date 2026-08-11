expenses = [250, 1200, 450, 800, 150, 2000, 350]
total_expense=sum(expenses)
high_expense=max(expenses)
low_expense=min(expenses)
avg_expense=total_expense/len(expenses)
above_500=0
below_500=0
for i in range(len(expenses)): 
    if expenses[i]>500:
        above_500+=1
    else:
        below_500+=1
print(f"Total expense: ₹{total_expense}")
print(f"Highest expense: ₹{high_expense}")
print(f"Lowest expense: ₹{low_expense}")
print(f"Average expense: ₹{avg_expense}")
print(f"Expenses above ₹500: {above_500}")
print(f"Expenses below ₹500: {below_500}")
for i in range(len(expenses)):
    if expenses[i]>avg_expense:
        print(expenses[i])

