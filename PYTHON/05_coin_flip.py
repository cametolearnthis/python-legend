# Coin Flip - Control Flow

import random

num = random.randint(0, 10) # # RNGesus will give us a random number that is either 0 or 1

print(num)

if num > 5:
    print('Heads')
elif num < 5:
    print('Tails')
else:
    print('it is 5')

