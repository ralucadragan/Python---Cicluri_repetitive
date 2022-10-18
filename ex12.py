'''
12.
Aceeasi lista
Ordonati crescator lista fara sa folositi sort
Va puteti inspira vizual de aici
'''

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]

for i in range(0,len(alte_numere)):
    for j in range(i+1,len(alte_numere)):
        if (alte_numere[i] > alte_numere[j]):
            alte_numere[i], alte_numere[j] = alte_numere[j], alte_numere[i]
    print(alte_numere)
print(f' Lista sortata crescator este: {alte_numere}')