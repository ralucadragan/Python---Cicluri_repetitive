'''
1.
Avand lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Folositi un for ca sa iterati prin toata lista si sa afisati
‘Masina mea preferata este x’
Faceti acelasi lucru cu un for each
Faceti acelasi lucru cu un while

'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for i in range(0, len(masini)):
    print(f'Masina mea preferata este: {masini[i]}')

for i in masini:
    print(f'Masina mea preferata este: {i}')

i = 0
while i < len(masini):
    print(f'Masina mea preferata este: {masini[i]}')
    i = i+1
