# program read 5 numbers and put on a list, output =  show the higher value and the lower value and their positions
values = []
higher = lower = pos_lower = pos_higher = 0
for c in range(0, 5):
    while True:
         try:
            values.append(int(input('Value: ')))
            break
         except ValueError:
              print('This is not a valid number')
    if c == 0:
         higher = lower = values[c]
         pos_lower = pos_higher = c
    elif values[c] > higher:
         higher = values[c]
         pos_higher = c
    elif values[c] < lower:
         lower = values[c]
         pos_lower = c
print(values)
print(f'the higher value its  {higher} and its at the position {pos_higher}')
print(f'the lower value its {lower} and its at the position {pos_lower}')
