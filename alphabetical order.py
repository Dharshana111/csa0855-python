def sort_names(names, order):
    if order == 'A':
        names.sort()
    elif order == 'D':
        names.sort(reverse=True)
    else:
        print("Invalid order choice! Please enter 'A' for Ascending or 'D' for Descending.")
        return

    for name in names:
        print(name)

names = input("Enter the list of names (separate by commas): ").split(',')
names = [name.strip() for name in names]

order = input("Order (A/D): ").upper()

sort_names(names, order)
