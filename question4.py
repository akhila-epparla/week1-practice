text=input("Enter the text: ")
u_count=0
l_count=0
digit_count=0
spaces_count=0
other_characters_count=0
for i in text:
    if(i.isupper()):
        u_count+=1
    elif(i.islower()):
        l_count+=1
    elif(i.isdigit()):
        digit_count+=1
    elif(i.isspace()):
        spaces_count+=1
    else:
        other_characters_count+=1
print(f"Uppercase letters: {u_count}")
print(f"Lowercase letters: {l_count}")
print(f"Digits: {digit_count}")
print(f"Spaces: {spaces_count}")
print(f"Other characters: {other_characters_count}")
