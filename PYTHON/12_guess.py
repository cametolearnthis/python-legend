 # Loop

tries = 0

guess = 0

while guess != 6 and tries < 3:
    guess = int(input('Guess the number: '))
    tries = tries + 1

    if guess == 6:
       print('You got it!')

    elif tries == 3:
        print('Too many guesses!')

    else:
        print('Try again!')
               

     
    

