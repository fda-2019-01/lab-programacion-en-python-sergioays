##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##
data = open('data.csv', 'r').readlines()
data = [line.replace('\t', ' ') for line in data]
data = [line.replace('\n', '') for line in data]
data = [line.split(' ') for line in data]
fecha = [line[2].split('-') for line in data]
mes = sorted(set([line[1] for line in fecha]))
cant = [line[1] for line in fecha]
for n in mes:
    print(str(n)+','+str(cant.count(n)))