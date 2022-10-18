'''
Ghicitoare de numar
numar_secret = Generati un numar random intre 1 si 30
Numar_ghicit = None
Folosind un while
   User alege un numar
   Programul ii spune:
Nr secret e mai mare
Nr secret e mai mic
Felicitari! Ai ghicit!
'''
import random

numar_secret = random.randrange(1,7)
numar_ghicit = True

while numar_ghicit:
    numar_ghicit = int(input('Alege un nr: '))
    if numar_secret > numar_ghicit:
        print('Numarul secret este mai mare.')
    elif numar_secret < numar_ghicit:
        print('Numarul sectet este mai mic')
    else:
        print('Felicitari! Ai ghicit!')


