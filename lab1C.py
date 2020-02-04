#Dylan Grafius    1/12/2018
#CSC131-005
#Purpose: The goal of thie program is to ask the user to provide a integer base and an integer exponent. Then it will display the the base raised to that exponent.
number= int(input("What base?"))
a= int(input("What power?"))
b= (number**a)
print(number,"raised to the power of",a,"is",b)
