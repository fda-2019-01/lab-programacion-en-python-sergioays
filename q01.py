##
## Imprima la suma de la segunda columna.
##
data = open('data.csv', 'r').readlines()
data = [line.replace('\t', ' ') for line in data]
data = [line.replace('\n', '') for line in data]
data = [line.split(' ') for line in data]
suma = sum([int(line[1]) for line in data])
print(suma)