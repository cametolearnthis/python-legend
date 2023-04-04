# pH Levels - Operators

import random

#ph = random.randint(0, 14)

#print(ph)

ph = int(input('Enter a value between 0 and 14: '))

print(ph)

if ph > 7:
    print('Basic')
elif ph < 7:
    print('Acidic')
else:
    print('Neutral')
    

