def check_prime(n):
    if n <=1:
        return False
    
    for i in range(2, int(n**0.5) +1 ):
        if n%i == 0:
            return False
    
    return True

x = int(input("Enter any number: "))

if (check_prime(x)):
    print(f"{x} is a prime number.")
else:
    print(f"{x} is not a prime number.")