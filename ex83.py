# Create a program where the user enters any expression
# that uses parentheses. Your application should analyze
# whether the provided expression has correctly opened and closed parentheses in the right order.
# For example, if the expression is ((a+b) - c), it checks if all parentheses are correctly matched.
# If there's a mistake, it should provide feedback, such as missing parentheses or having extra parentheses.
e = []  # Creating a list named 'e' that will serve as a pile
expression = (str(input('Type an expression: '))).strip()  # User is going to type their expression
for symbol in expression:  # Symbol is going to verify if the expression has the '(' open and put it in the pile 'e'
    if symbol == '(':
        e.append('(')
    elif symbol == ')':
        if len(e) > 0:  # If the symbol ')' is found after the '(' open, the '(' will be removed from the pile
            e.pop()  # Meaning that when the pile 'e' is 0, that means the parentheses were open and closed correctly
        else:
            e.append(')')  # Otherwise, if the program doesn't find that the pile length is not 0, it will store the ')' closing the pile
if len(e) != 0:
    print('Your expression is incorrect')  # If 'e' is higher than 0, that means the expression is incorrect
else:
    print('Your expression is correct')
