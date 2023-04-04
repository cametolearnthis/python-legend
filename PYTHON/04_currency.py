# Currency 

yuan = int(input('What do you have left in yuan?: '))
yen = int(input('What do you have left in yen?: '))
won = int(input('What do you have left in won?: '))

yuan_exchange = yuan * 0.15
yen_exchange = yen * 0.0075
won_exchange = won * 0.00077

total = yuan_exchange + yen_exchange + won_exchange

print(total)

