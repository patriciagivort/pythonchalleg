# Create a program where the user can enter multiple numerical values and store them in a list. If the number already exists in the list, it will not be added. In the end, all values will be displayed in ascending order.
values = list()
answer = ' '
while True:
    n = int(input('Type a value: '))
    if n not in values:
        values.append(n)
    else:
        print('Value already in the list.')
    answer = str(input('Want to continue? Y/N: ')).strip().upper()
    if answer not in 'Y':
        break
values.sort()
print(values)
