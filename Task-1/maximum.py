a = list(map(int, input("Enter the list elements(spearated by spaces):").split())) #type: ignore

print(f"Given list is: {a}")

max1 = a[0]

for i in a:
    if (i > max1):
        max1 = i

print(f"Maximum element in the given list is: {max1}")