##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
data = open('data.csv', 'r').readlines()
data = [line.replace('\t', ' ') for line in data]
data = [line.replace('\n', '') for line in data]
data = [line.split(' ') for line in data]
let = [line[3].split(',') for line in data]
let_or = sorted(set(sum(let, [])))
busq = [line[1:4] for line in data]
b = []
for line in busq:
    b.append([line[0]] + line[2].split(','))
sol = []
for letra in let_or:
    inic = [letra]
    count = 0
    for line in b:
        if letra in line:
            count = count + int(line[0])
    inic = inic + [count]
    sol = sol + [inic]       
for line in sol:
    print(str(line[0])+","+str(line[1]))