'''
Avand dict
pret_masini = {
    'Dacia': 6800,
    'Lastun': 500,
    'Opel': 1100,
    'Audi': 19000,
    'BMW': 23000
}
Vine un client cu un buget de 15000 euro
Prezentati doar masinile care se incadreaza in acest buget
Iterati prin dict.items() si accesati masina si pretul
Printati Pentru un buget de sub 15000 euro puteti alege masina x
Iterati prin lista
'''

pret_masini = {'Dacia': 6800,'Lastun': 500,'Opel': 1100,'Audi': 19000,'BMW': 23000}
# masini_noi = {i:pret_masini[i] for i in pret_masini if pret_masini[i]<15000}
# print(masini_noi)
buget = 15000

for i in pret_masini:
    if pret_masini[i] < buget:
        print(f'Pentru un buget de sub {buget} puteti alege masinile: {i} care costa {[pret_masini[i]]}')