'''
5.
Modernizati parcul de masini
Creati o lista goala, masini_vechi
Iterati prin masini
Cand gasiti Lastun sau Trabant:
Salvati aceste masini in masini_vechi
Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
Printati Modele vechi: x
Modele noi: x
'''

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
masina1 = 'Trabant'
masina2 = 'Lastun'
masini_vechi =[]

for i in range(0,len(masini)):
    if masini[i] == masina1 or masini[i] == masina2:
        masini_vechi.append(masini[i])
        masini[i] = 'Tesla'
print(f'Modelele vechi sunt: {masini_vechi}')
print(f'Modelele noi sunt: {masini}')

for i in masini:
    if i == masina1 or i == masina2:
        masini_vechi.append(i)
        i = 'Tesla'
print(f'Modelele vechi sunt: {masini_vechi}')
print(f'Modelele noi sunt: {masini}')
