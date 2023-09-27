# Create a program that creates a 3x3 matrix and fills it with values entered by the user
# Finally, display the matrix with the correct formatting

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for c in range(3):
    for i in range(3):
        n = int(input(f'Enter the value for row {c} and column {i}: '))
        matriz[c][i] = n

print("Matrix:")
for row in matriz:
    for value in row:
        print(f'[{value}]', end=' ')
    print()
