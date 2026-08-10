n=int(input())
even_count=0
odd_count=0
for i in range(1,n+1):
    if(7*i%2==0):
        even_count+=1
    else:
        odd_count+=1
print(f"Even_results: {even_count}")
print(f"Odd_results: {odd_count}")
