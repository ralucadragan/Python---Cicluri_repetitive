'''
4.
Aceasi lista
Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun.
Daca masina e Trabant sau Lastun
   Folositi un cuvant cheie care sa dea skip la ce urmeaza
Printati S-ar putea sa va placa masina x
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masina1 = 'Trabant'
masina2 = 'Lasturn'

for i in masini:
    if i == masina1 or i == masina2:
        continue
    print(f'S-ar putea sa va placa masina: {i}')
