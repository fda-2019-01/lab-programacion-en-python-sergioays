##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
data = open('data.csv', 'r').readlines()
data = [line.replace('\t', ' ') for line in data]
data = [line.replace('\n', '') for line in data]
data = [line.split(' ') for line in data]
letra = sorted(set([line[0] for line in data]))
for n in letra:
    suma = sum([int(line[1]) for line in data if line[0] == n])
    print(str(n)+','+str(suma))