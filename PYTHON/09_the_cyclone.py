# Logical Operators

#if hunger > 4 and anger > 1:
#    print('Hangry')

height = int(input('What is your height?: '))
credits = int(input('How many credits do you have?: '))
with_taller_person = bool(input('Are you with a taller person? '))

# if height >= 137 and credits >= 10:
#     print('Enjoy the ride!')
# elif height < 137:
#     print('You are not tall enough to ride.')
# elif credits < 10:
#     print('You don\'t have enough credits to ride.')
# else:
#     print('Invalid data.')

if height >= 137 and credits >= 10:
    print('Enjoy the ride!')
elif height < 137:
    if height < 100 or with_taller_person == False: 
        print('You are not tall enough to ride yet.')
    elif height >= 100 and with_taller_person == True:
        print('Enjoy the ride!')
elif credits < 10:
    print('You don\'t have enough credits to ride.')
    








