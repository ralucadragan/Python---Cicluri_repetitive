'''
11.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Iterati prin lista alte_numere
Populati corect celelalte liste
Afisati cele 4 liste la final
'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

numere_pare = [i for i in alte_numere if i%2 == 0]
print(f'Lista cu numere pare este: {numere_pare}')
numere_impare = [i for i in alte_numere if i%2 > 0]
print(f'Lista cu numere impare este: {numere_impare}')
numere_pozitive = [i for i in alte_numere if i > 0]
print(f'Lista cu numere pozitive este: {numere_pozitive}')
numere_negative = [i for i in alte_numere if i < 0]
print(f'Lista cu numere negative este: {numere_negative}')

print('-----------------------------------------------------------')

numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for i in alte_numere:
    if i%2 == 0:
        numere_pare.append(i)
    else:
        numere_impare.append(i)
    if i >= 0:
        numere_pozitive.append(i)
    else:
        numere_negative.append(i)
print(f'Lista cu numere pare este: {numere_pare}')
print(f'Lista cu numere impare este: {numere_impare}')
print(f'Lista cu numere pozitive este: {numere_pozitive}')
print(f'Lista cu numere negative este: {numere_negative}')