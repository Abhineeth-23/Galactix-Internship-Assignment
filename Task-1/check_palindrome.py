def check_palindrome(s):
    s = s.lower()
    
    cleaned = ""

    for a in s:
        if a.isalnum():
            cleaned += a

    reverse = "" 

    for a in cleaned:
        reverse = a + reverse

    return cleaned == reverse

str1 = input("Enter your string or number: ")

if check_palindrome(str1):
    print(f"'{str1}' is a palindrome.")
else:
    print(f"'{str1}' is not a palindrome.")