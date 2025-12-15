str1 = input("Enter your string: ")

reverse = "" 

for a in str1:
    reverse = a + reverse

print(f"Reversed string: {reverse}")