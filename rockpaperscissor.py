import random

user_win=0
computer_win= 0
option = ['rock','papper','scissor']

while True:
    user_in = input("Enter Rock/Paper/Scissor or q to quit ")
    if user_in == 'q':
        break #break you out from the loop
    
    if user_in not in option:
        #print('Enter Rock/Paper/Scissor or q to quit ')
        continue #restart the loop

    rand_num = random.randint(0,2)
    computer_choose = option[rand_num]
    print('computer picked',computer_choose+'.')

    if user_in=='papper' and computer_choose=='rock':
        print('You won.')
        user_win=+1

    elif user_in=='rock' and computer_choose=='scissor':
        print('You won.')    
        user_win=+1

    elif user_in=='scissor' and computer_choose=='papper':
        print('You won.')  
        user_win=+1
    else:
        print("you lost computer wins.")  
        computer_win=+1

    
print('You won ',user_win,' times.')
print('Computer won ',computer_win,' times.')
print('Thankyou for palying')