'''
9.
Aceeasi lista
Iterati prin ea
Afisati cel mai mare numar
(nu aveti voie sa folositi max)
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
nr = 0
for i in numere:
    if i > nr:
       nr = i
print(f'Cel mai mare numar este {nr}')