# Sorting Hat 
import emoji

gryf = 0
rav = 0
huff = 0
sly = 0

print(emoji.emojize('======== :star: SORTING HAT :star: ========\nAnswer the test and you will be sorted into your Hogwarts house: '))

q1 = (input('Question 1. Do you like dawn or dusk? '))

if q1.casefold() == 'dawn':
    gryf += 1
    rav += 1
elif q1 == 'dusk':
    huff += 1
    sly += 1
else:
    print('Wrong input.')

q2 = (input('Question 2. When I’m dead, I want people to remember me as \n The Good \n The Great \n The Wise \n The Bold \n Type your answer: '))

if q2 == 'the good':
    huff += 2
elif q2 == 'the great':
    sly += 2
elif q2 == 'the wise':
    rav += 2
elif q2 == 'the bold':
    gryf += 2
else:
    print('Wrong input.')

q3 = (input('Question 3. Which kind of instrument most pleases your ear? \n The violin \n The trumpet \n The piano \n The drum \n Type your answer: '))

if q3 == 'the violin':
    sly += 4
elif q3 == 'the trumpet':
    huff += 4
elif q3 == 'the piano':
    rav += 4
elif q3 == 'the drum':
    gryf += 4
else:
    print('Wrong input.')

print('Hold your breath...')

if gryf > huff and gryf > rav and gryf > sly:
    print(emoji.emojize('You are Balenciaga, Harry :lion:'))
elif rav > huff and rav > gryf and rav > sly:
    print(emoji.emojize('You are a Ravenclaw! :eagle:'))
elif huff > rav and huff > gryf and huff > sly:
    print(emoji.emojize('You are a Hufflepuff!:badger:'))
elif sly > huff and sly > gryf and sly > rav:
    print(emoji.emojize('You are a Slytherin!:snake:'))
else:
    print('Wrong input')




    







    