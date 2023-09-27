# Enhance the previous challenge by displaying, at the end:
# a) the sum of all even values entered,
# b) the sum of the values in the third column,
# c) the highest value in the second row.
matrix = [[], [], []]
sum_even = col_sum = max_second_row = 0
for row in range(0, 3):
    for col in range(0, 3):
        num = int(input(f'Enter a value for column {col} and row {row}: '))
        matrix[row].append(num)

        if num % 2 == 0:
            sum_even += num

        if col == 2:
            col_sum += num

        if row == 1:
            if col == 0:
                max_second_row = num
            elif matrix[1][col] > max_second_row:
                max_second_row = num

for row in matrix:
    for num in row:
        print(f'[{num:^5}]', end='  ')
    print()

print(f'The sum of even values is {sum_even}')
print(f'The sum of values in the third column is {col_sum}')
print(f'The highest value in the second row is {max_second_row}')
