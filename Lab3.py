###########################################
#Dylan Grafius         1/31/2018
#CSC 131-005
#Problem 1: The purpose of this program is to evaluate the length of the 3 sides of a triangle that the user will enter and state whether it is an equilateral or not.
print('Problem 1: Using if statements')
side1 = int(input('Enter your first side:'))
side2 = int(input('Enter your second side:'))
side3 = int(input('Enter your third side:'))
if side1 == side2 and side2 == side3 and side3 == side1:
    print('This is an equilateral')
else:
    print('This is not an equilateral')

print()

#Problem 2: The purpose of this program is to display a word depending on what letter the user enters.
print('Problem 2: Using nested if statements')
letter = input('Enter "A" for apple, "B for banana, or "C" for coconut:')
if letter == 'A' or letter == 'a':
    print('Apple')
if letter == 'B' or letter == 'b':
    print('Banana')
if letter == 'C' or letter == 'c':
    print('Coconut')

print()

#Problem 3: The purpose of this program is to display a word depending on what letter the user enters.
print('Problem 3: Using elif headers instead')
word = input('Enter "A" for apple, "B for banana, or "C" for coconut:')
if word == 'A' or word == 'a':
    print('Apple')
elif word == 'B' or word == 'b':
    print('Banana')
elif word == 'C' or word == 'c':
    print('Coconut')
