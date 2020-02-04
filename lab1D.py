#Dylan Grafius       1/16/2018
#CSC131-004
#Purpose: The purpose of this program is to convert binary into its base 10 value.
a = int(input('Enter leftmost digit:'))
num1=a*(2**0)
b = int(input('Enter the next digit:'))
num2=b*(2**1)
c = int(input('Enter the next digit:'))
num3=c*(2**2)
d = int(input('Enter the next digit:'))
num4=d*(2**3)
final = (num1 + num2 + num3 + num4)
print('The value is',final)



