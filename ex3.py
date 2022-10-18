'''
3.
Aceeasi lista,
Vine un cumparator care doreste sa cumpere un Mercedes
Iterati prin ea prin for each
Daca masina e mercedes (if)
   Printam ‘am gasit masina dorita de dvs’
   Iesim din ciclu folosind un cuvant cheie care face acest lucru
Altfel
   Printam Am gasit masina X. Mai cautam
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masina_dorita = 'Mercedes'

for i in masini:
    if i == masina_dorita:
        print('Am gasit masina dorita de d-voastra')
        break
    else:
        print(f'Nu am gasit {masina_dorita}, mai cautam')
