#Dylan Grafius             2/15/2018
#CSC 131-005
#Program Assignment 1
################################################
print('Game of Lucky Seven')
print('These are the rules:')
print('1. Roll the dice and add up the dots that you roll.')
print('2. If the dots add up to 7 then you win $4.')
print('3. If the dots do not add up to 7 then you lose $1.')
#The statements above will display as shown on the screen when running the program so that the user knows the rules to the game. 
roll = 0
#Setiing the variable equals to 0 will help me make sure that the number it prints is correct.
start = int(input('Please enter the amount of money you want to play with:'))
while start > 0:
    import random
    a = random.randint(1,7) #This creates the range of numbers to be generated.
    b = random.randint(1,7)
    if (a + b) == 7:
        #If the 2 numbers are added up and equal 7, then the 
        print('The numbers are', a,'and',b)
        print('Congratulations, you win $4!')
        #This function will display everytime that the user wins to let the user know that they won $4.
        start += 4
        #This operation adds 4 to whatever the user enters everytime the 2 random generated numbers equals 7.
        roll += 1
        #This operation counts the number of times the user rolls the dice.
        print('Your amount is now:', '$',start)
        print('You rolled', roll,'times.')    
    if (a + b) != 7:
        #This says that if the 2 numbers do not equal 7, then the following happens. 
        print('The numbers are', a,'and',b)
        print('Sorry, you lose $1.')
        #This function will display everytime that the user loses to let the user know that they lost $1.
        start -= 1
        #This operation subtracts 1 from whatever the user enters if the 2 numbers do not equal 7.
        roll += 1
        print('Your amount is now:', '$',start)
        if start == 0:
            #Once the user runs out of money, the program will print this starement.
            print('Thank you for playing, you rolled', roll,'times.') 
    
        
