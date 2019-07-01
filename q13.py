##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
data = open('data.csv', 'r').readlines()
data = [line.replace('\t', ' ') for line in data]
data = [line.replace('\n', '') for line in data]
data = [line.split(' ') for line in data]
num5 = [line[4].split(',') for line in data]
num5 = [[elem[4] for elem in line] for line in num5]
num5 = [[int(elem) for elem in line] for line in num5]
letras = [line[0] for line in data]
for n in range(len(letras)):
    print(str(letras[n])+","+str(sum(num5[n])))