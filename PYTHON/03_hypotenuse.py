from math import sqrt

a = int(input('Give me the value of the first cathetus: '))
b = int(input('Give me the value of the other cathetus: '))
c = sqrt(a ** 2 + b ** 2) 

print('The hypotenuse is:', c)


a = int(input('Give me the value of the first cathetus: '))
b = int(input('Give me the value of the other cathetus: '))
c = (a ** 2 + b ** 2)**0.5

print('The hypotenuse is:', c)
