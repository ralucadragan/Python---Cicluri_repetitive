'''
7.
Avand lista
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterati prin ea
Afisati de cate ori apare 3
(nu aveti voie sa folositi count)
'''

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
y = 0

for i in numere:
    if(i==3):
        y=y+1
print(f'Numarl cautat apare de {y} ori.')