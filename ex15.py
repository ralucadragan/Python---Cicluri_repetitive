'''
15.
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]
Iterati prin lista 2d
Printati ‘Cifra curenta este x’
(hint: nested for - adica for in for)
'''

tastatura_telefon = [[1, 2, 3],[4, 5, 6],[7, 8, 9],[0]]

for i in range(len(tastatura_telefon)):
    for j in range(len(tastatura_telefon[i])):
        print(f' Cifra curenta este {tastatura_telefon[i][j]}.')

