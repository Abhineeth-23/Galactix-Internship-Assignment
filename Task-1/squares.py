def squares(l):
    sq = {}
    for num in l:
        sq[num] = num*num
    
    return sq

l1 = list(map(int, input("Enter your numbers(separated by spaces): ").split()))

print(f"\nSquares of given numbers: \n{squares(l1)}")