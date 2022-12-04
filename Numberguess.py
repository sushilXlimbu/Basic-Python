import random

top_of_range = input("Enter the top of the range: ")

if top_of_range.isdigit():
    top_of_range=int(top_of_range)

    if top_of_range <= 0:
        print('Enter number greater than 0 next time')
        quit()
else:
     print('Please enter number next time')
     quit()


random_num= random.randint(0,top_of_range)

while True:
    number = input('Guess the number: ')
   
    if number.isdigit():
        number=int(number)
        if number <= 0:
            print('Enter number greater than 0 next time')
            quit()
    else:
        print('Please enter number next time')
        quit()

    if number == top_of_range:
        print('Congrats You are right')    
        break    

    else:
        print('Try again!!!!')  

 