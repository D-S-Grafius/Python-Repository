#######################################
#Dylan Grafius        1/24/2018
#Section 005

#Problem 1: The purpose of this problem is for the user to enter 2 values and have the reult of the first number divided by the second number shown.
number1 = int(input('Enter first number:'))
number2 = int(input('Enter second number:'))
value = number1/number2
print(format(value, '.3f'))

#Problem 2: The purpose of this problem is for the user to enter 2 floating-point values and have it display the value of the first number divided by the seconf number.
number1 = float(input('Enter first floating-point number:'))
number2 = float(input('Enter second floating-point number:'))
value = number1/number2
print(format(value, '.5f'))

#Problem 3: The purpose of this problem is for the user to enter two floating-point values and have the results for the fist value divided by the second value shown.
number1 = float(input('Enter first floating-point number:'))
number2 = float(input('Enter second floating-point number:'))
value = number1/number2
print(format(value, '.6e'))

#Problem 4: The purpose of this problem is for the user to enter an uppercase and a lowercase letter and have the unicode displayed below.
L1 = input('Enter uppercase letter:')
L2 = input('Enter lowercase letter:')
print(ord(L1))
print(ord(L2))

#Problem 5: The purpose of this problem is for the user to enter twp integer values and have the results of several arithmetic operations shown below.
number1 = int(input('Enter first number:'))
number2 = int(input('Enter second number:'))
value1 = number1+number2
value2 = number1-number2
value3 = number1*number2
value4 = number1/number2
value5 = number1//number2
value6 = number1%number2
value7 = number1**number2
print(number1,'+',number2,'=', value1)
print(number1,'-',number2,'=', value2)
print(number1,'*',number2,'=', value3)
print(number1,'/',number2,'=', format(value4, '.2f'))
print(number1,'//',number2,'=', value5)
print(number1,'%',number2,'=', value6)
print(number1,'**',number2,'=', value7)
