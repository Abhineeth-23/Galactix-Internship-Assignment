def unique_list(l):
    unique = []

    for ele in l:
        if ele in unique:
            continue
        else:
            unique.append(ele)
    
    return unique

l1 = list(input("Enter the elements of your list(separated by spaces): ").split())

print(f"\nAfter removing duplicates from {l1},\nResult: {unique_list(l1)}")