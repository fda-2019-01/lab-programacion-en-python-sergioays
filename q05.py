##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
data = open('data.csv', 'r').readlines()
data = [line.replace('\t', ' ') for line in data]
data = [line.replace('\n', '') for line in data]
data = [line.split(' ') for line in data]
letra = sorted(set([line[0] for line in data]))
for n in letra:
    maximo = max([int(line[1]) for line in data if line[0] == n])
    minimo = min([int(line[1]) for line in data if line[0] == n])
    print(str(n)+','+str(maximo)+','+str(minimo))