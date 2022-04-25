from math import*

N = int(input('введи число'))
for i in [2,3,4,5,9]:
    if N % i == 0:
        print('ДЛИМОСТЬ НА',i,'ДА')
    else:
        print('ДЛИМОСТЬ НА',i,'НЕТ')
    