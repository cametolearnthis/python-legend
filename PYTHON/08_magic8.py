# Magic 8 - Random

import random

question = input('Ask me a question: ')

magic_8_ball = ['Yes - definitely.', 'It is decidedly so.', 'Without a doubt.','Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

answer = random.choice(magic_8_ball)

print('Magic 8 Ball says: ' + answer)




