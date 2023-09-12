# Create a program where the user can enter five numerical values and add them to a list, already in the correct insertion position (without using sort()). Finally, display the sorted list on the screen.
list = []
for c in range(0, 5):
    n = int(input('Value: '))
    if c == 0 or n > list[-1]:
        list.append(n)
    else: 
        i = 0
        while i < len(list):
            if n <= list[i]:
                list.insert(i, n)
                break
            i += 1
print(list)
