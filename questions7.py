original= [10, 10, 20, 20, 20, 30, 10, 10, 40]
new=[]
for i in range(len(original)):
    if  not new or original[i]!=new[-1]:
        new.append(original[i])
print("Original List:")
print(original)
print("Result:")
print(new)