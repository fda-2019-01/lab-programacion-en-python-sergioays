##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
data = open('data.csv', 'r').readlines()
data = [line.replace('\t', ' ') for line in data]
data = [line.replace('\n', '') for line in data]
data = [line.split(' ') for line in data]
col4 = [line[3].split(',') for line in data]
col5 = [line[4].split(',') for line in data]
for n in range(len(data)):
    print(str(data[n][0])+','+str(len(col4[n]))+','+str(len(col5[n])))