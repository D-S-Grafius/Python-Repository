#Dylan Grafius              2/21/2018
#CSC 131-005
#######################################
list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ']
list2 = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', ' ']

letval = input('This program will convert between English and Morse code. \n (E)nglish to Morse code, or (M)orse to English?')

while letval != 'E' and letval != 'M' and letval != 'e' and letval != 'm':
    letval = input('\nInvalid Input - Enter E or M: ')


english = (letval == 'E' or letval == 'e')
nat = input('Enter code or English (q to quit) : ')
output = ''
while nat != 'q':
    nat = nat.upper()
    if english:
        for char in range(len(nat)):
            for i in range(len(list1)):
                if nat[char] == list1[i]:
                    print(list2[i])
    else:
        for i in range(len(list2)):
            if nat == list2[i]:
                #print(list1[i])
                output += (list1[i])
    nat = input('Enter code or English (q to quit) : ')

print(output)

        
