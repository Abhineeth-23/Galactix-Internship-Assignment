def even_numbers(l):
    evens = []

    for ele in l:
        if ele % 2 == 0:
            evens.append(ele)
    
    return evens

l1 = list(map(int, input("Enter your numbers(separated by spaces): ").split()))

print(f"Even numbers from the given list are: {even_numbers(l1)}")