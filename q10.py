##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
data = open('data.csv', 'r').readlines()
data = [line.replace('\t', ' ') for line in data]
data = [line.replace('\n', '') for line in data]
data = [line.split(' ') for line in data]
clave = [line[4].split(',') for line in data]
clave = [[elem[:3] for elem in line] for line in clave]
clave = sum(clave, [])
claveorg = sorted(set(clave))
for n in claveorg:
    rep = [line for line in clave if line == n].count(n)
    print(str(n)+','+str(rep))