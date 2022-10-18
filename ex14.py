'''
14.
Alegeti un numar de la tastatura
Ex:7
Scrieti un program care sa genereze in consola urmatoarea piramida
1
22
333
4444
55555
666666
7777777

Ex:3
1
22
333
'''

# trebuie 2 foruri: 1 pt linii si 1 pt coloane
n = int(input('Alegeti nr dorit: '))
for i in range(n+1):
    for j in range(i):
        print (i, end='')
    print()
