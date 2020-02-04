#Dylan Grafius              2/7/2018
#CSC131-005

print('Problem 1: Practice using a while loop that adds up even numbers between 100 and 200 which the total should equal 7650')
current = 100
total = 0
while current <= 200:
    total = total + current
    current = current + 2
print('The final value is:',total)
################################################

print('Problem 2: Summing the positive values entered by the user that are less than 100')
a = 0
b = 0
while a <= 100 or b <= 100:
    a = int(input('Enter a number (enter -1 to quit):'))
    b = b + a
    if a == -1:
        print('The sum is:',b)
        break
################################################

print('Problem 3: Count the number of poisitive and negative numbers that the user enters.')
x = 0
y = 0
while True:
    num = int(input('Enter a number or enter 0 to quit:'))
    if num >= 1:
        x+= 1
    elif num <=1:
        y += 1
    elif num == 0:
        print('positive numbers:',x)
        print('negative numbers:',y)
        break
###############################################
    
print('Problem 4: Nested while loops')
q=1
w=10
while q<=100:
    while(w>0):
        print(q,end='')
        q=q+1
        w=w-1
    w=10
        
